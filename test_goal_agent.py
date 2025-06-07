from agents import goal_interpreter_agent

sample = "I want to become a Prompt Engineer in 2 months"
result = goal_interpreter_agent(sample)

print("Goal:", result["goal"])
print("Duration (weeks):", result["duration_weeks"])
print("Plan:")
for i, week in enumerate(result["weekly_plan"], 1):
    print(f"  Week {i}: {week}")
