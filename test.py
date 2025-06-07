from utils.plan_exporter import export_plan_to_excel
from agents import reminder_agent
from agents import (
    goal_interpreter_agent,
    preference_collector_agent,
    source_fetcher_agent,
    path_builder_agent,
    weekly_task_generator_agent
)
sample = "I want to become a Prompt Engineer in 2 months"
goal_result = goal_interpreter_agent(sample)

print("Goal:", goal_result["goal"])
print("Duration (weeks):", goal_result["duration_weeks"])
print("\nCollecting user preferences...\n")

preferences = preference_collector_agent()
print("User Preferences:", preferences)

print("\nFetching resources based on preferences...\n")
resources = source_fetcher_agent(goal_result["weekly_plan"], preferences)
final_plan = path_builder_agent(goal_result, resources)

print("\nGenerating weekly tasks...\n")
plan_with_tasks = weekly_task_generator_agent(final_plan)

for week in plan_with_tasks:
    print(f"\nWeek {week['week']}: {week['topic']}")
    print("Task:", week["task"], f"({week['task_type']})")
print("\nExporting to Excel...")
export_plan_to_excel(plan_with_tasks)

email = reminder_agent()
if email:
    print(f"\nWeekly reminder will be sent to: {email}")