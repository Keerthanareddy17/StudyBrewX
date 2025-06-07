import pandas as pd

def export_plan_to_excel(plan_with_tasks: list, filename="studybrewx_plan.xlsx"):
    data = []
    for week in plan_with_tasks:
        data.append({
            "Week": week["week"],
            "Topic": week["topic"],
            "Task": week["task"],
            "Task Type": week["task_type"],
            "YouTube Links": ", ".join(week.get("youtube_links", [])) if "youtube_links" in week else "",
            "Blog Links": ", ".join(week.get("blog_links", [])) if "blog_links" in week else "",
        })
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Plan exported successfully to: {filename}")
