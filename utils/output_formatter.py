def build_learning_path(weekly_goals, weekly_resources):
    full_plan = []

    for i, (goal, resources) in enumerate(zip(weekly_goals, weekly_resources), start=1):
        week_data = {
            "week": i,
            "topic": goal,
            "youtube": resources.get("youtube", []),
            "blogs": resources.get("blogs", [])
        }
        full_plan.append(week_data)

    return full_plan
