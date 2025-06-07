import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from utils.output_parser import parser, format_instructions, GoalPlan
from prompts import goal_prompt_template, preference_prompt_template, weekly_task_prompt_template
from utils.fetch_resoucres import fetch_youtube_resources, fetch_blog_resources
from utils.output_formatter import build_learning_path
import json
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def goal_interpreter_agent(user_input: str) -> dict:
    prompt = PromptTemplate(
        template=goal_prompt_template,
        input_variables=["user_input"],
        partial_variables={"format_instructions": format_instructions}
    )

    formatted = prompt.format(user_input=user_input)
    response = llm.invoke(formatted)

    try:
        parsed_raw = parser.parse(response.content)
        validated = GoalPlan(**parsed_raw)
        return validated.dict()
    except Exception as e:
        print("⚠️ Parsing or validation failed.")
        print("Raw response content:\n", response.content)
        raise ValueError(f"Goal Interpreter Agent failed to parse response: {e}")
def preference_collector_agent() -> dict:
    prompt = PromptTemplate(
        template=preference_prompt_template,
        input_variables=[]
    )
    response = llm.invoke(prompt.format())

    try:
        return json.loads(response.content)  # OR use json.loads() after verifying valid JSON
    except Exception as e:
        print("Failed to parse user preferences.")
        print("Response:\n", response.content)
        raise ValueError(f"Preference Collector Agent failed: {e}")
    
def source_fetcher_agent(weekly_plan: list[str], preferences: dict) -> list[dict]:
    weekly_resources = []
    prefer_videos = preferences["preferred_content"].lower() in ["youtube videos", "videos", "visual", "mixed"]
    prefer_blogs = preferences["preferred_content"].lower() in ["blogs", "blog articles", "reading", "mixed"]

    for i, topic in enumerate(weekly_plan, start=1):
        search_query = topic.replace(f"Week {i}:", "").strip()

        youtube_results = fetch_youtube_resources(search_query) if prefer_videos else []
        blog_results = fetch_blog_resources(search_query) if prefer_blogs else []

        weekly_resources.append({
            "week": i,
            "topic": search_query,
            "youtube_videos": youtube_results,
            "blogs": blog_results
        })

    return weekly_resources

def path_builder_agent(goal_data: dict, resource_data: list):
    weekly_goals = goal_data["weekly_plan"]
    learning_path = build_learning_path(weekly_goals, resource_data)
    return {
        "goal": goal_data["goal"],
        "duration_weeks": goal_data["duration_weeks"],
        "learning_path": learning_path
    }

def weekly_task_generator_agent(final_plan: dict) -> list[dict]:
    enriched_weeks = []
    for week in final_plan["learning_path"]:
        prompt = weekly_task_prompt_template.format(week_info=week["topic"])
        response = llm.invoke(prompt)

        try:
            task_data = json.loads(response.content.strip("```json\n").strip("```"))
            enriched_weeks.append({
                **week,
                "task": task_data["task"],
                "task_type": task_data["type"]
            })
        except Exception as e:
            print(f"Failed to parse task for Week {week['week']}: {e}")
            enriched_weeks.append({**week, "task": "No task generated", "task_type": "N/A"})

    return enriched_weeks

def reminder_agent():
    user_input = input("📩 Would you like to receive weekly reminders? (yes/no): ").strip().lower()
    if user_input != "yes":
        print("🔕 Reminders skipped.")
        return None
    
    email = input("✉️ Enter your email address: ").strip()
    if "@" not in email:
        print("Invalid email. Skipping reminders.")
        return None
    
    print(f"Email '{email}' recorded. Reminders will be sent weekly.")
    return email
