import streamlit as st
from agents import (
    goal_interpreter_agent,
    preference_collector_agent,
    source_fetcher_agent,
    path_builder_agent,
    weekly_task_generator_agent
)
import pandas as pd
import io

st.set_page_config(page_title="📚 StudyBrewX", layout="wide")
st.title("📚 StudyBrewX: Your Personalized Learning Path Generator")
st.markdown("""
Welcome to **StudyBrewX**! 🎓  
Tell us what you want to learn and how you prefer to study,  
and we'll craft a tailored weekly study plan with curated resources and actionable tasks.
""")

# Input section
with st.form("user_input_form"):
    user_goal = st.text_input("🎯 What is your learning goal? (e.g., Become a Prompt Engineer in 2 months)", "Become a Data Analyst in 2 months")
    preferred_type = st.selectbox("📖 Preferred content type", ["Mixed (Videos & Blogs)", "Only Blogs", "Only Videos"])
    submitted = st.form_submit_button("🔍 Generate my Study Plan")

if submitted:
    with st.spinner("🧠 Understanding your learning goal..."):
        goal_data = goal_interpreter_agent(user_goal)

    with st.spinner("💬 Capturing your preferences..."):
        preferences = {"preferred_content": preferred_type}

    with st.spinner("🔍 Fetching resources for each week..."):
        weekly_resources = source_fetcher_agent(goal_data["weekly_plan"], preferences)

    with st.spinner("🛠️ Generating a learning path..."):
        raw_plan = path_builder_agent(goal_data, weekly_resources)

    with st.spinner("📝 Designing weekly tasks..."):
        final_plan = weekly_task_generator_agent(raw_plan)

    st.success(f"✅ Learning plan ready for: {goal_data['goal']}")
    st.info(f"📆 Duration: {goal_data['duration_weeks']} weeks")

    def export_plan_to_excel_bytes(plan_with_tasks):
        output = io.BytesIO()
        data = []

        for week in plan_with_tasks:
            topic = week["topic"]
            if topic.lower().startswith(f"week {week['week']}:"):
                topic = topic.split(":", 1)[1].strip()

            data.append({
                "Week": week["week"],
                "Topic": topic,
                "Task": week["task"],
                "Task Type": week["task_type"],
                "YouTube Links": ", ".join([v['url'] for v in week.get("youtube", [])]),
                "Blog Links": ", ".join([b['url'] for b in week.get("blogs", [])]),
            })

        df = pd.DataFrame(data)
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Study Plan')

        output.seek(0)
        return output

    for week_info in final_plan:
        topic = week_info["topic"]
        if topic.lower().startswith(f"week {week_info['week']}:"):
            topic = topic.split(":", 1)[1].strip()

        st.markdown(f"### 📅 Week {week_info['week']}: {topic}")
        st.write(f"**🛠️ Task:** {week_info.get('task', 'No task generated')}")
        st.write(f"**📂 Task Type:** {week_info.get('task_type', 'N/A')}")

        if week_info.get("youtube"):
            st.write("**▶️ YouTube Videos:**")
            for vid in week_info["youtube"]:
                st.markdown(f"- [{vid['title']}]({vid['url']})")

        if week_info.get("blogs"):
            st.write("**📝 Blog Articles:**")
            for blog in week_info["blogs"]:
                st.markdown(f"- [{blog['title']}]({blog['url']})")

        st.markdown("---")

    excel_bytes = export_plan_to_excel_bytes(final_plan)
    st.download_button(
        label="📥 Export this plan to Excel",
        data=excel_bytes,
        file_name="studybrewx_plan.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
