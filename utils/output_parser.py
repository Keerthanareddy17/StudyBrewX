from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from pydantic import BaseModel, validator
from typing import List

# Define schema for LLM response
goal_schema = [
    ResponseSchema(name="goal", description="The career goal or target role."),
    ResponseSchema(name="duration_weeks", description="Number of weeks for preparation."),
    ResponseSchema(name="weekly_plan", description="A breakdown of topics or learning goals for each week.")
]

# Use LangChain parser to generate format instructions
parser = StructuredOutputParser.from_response_schemas(goal_schema)
format_instructions = parser.get_format_instructions()


# Optional but useful: Pydantic validation model
class GoalPlan(BaseModel):
    goal: str
    duration_weeks: int
    weekly_plan: List[str]

    @validator("weekly_plan", pre=True)
    def ensure_list(cls, v):
        if isinstance(v, str):
            lines = [line.strip("-• ").strip() for line in v.split("\n") if line.strip()]
        else:
            lines = [line.strip() for line in v if line.strip()]
        
        cleaned = []
        for line in lines:
            # Remove duplicate "Week X: Week X:" pattern
            parts = line.split(":")
            if len(parts) >= 3 and parts[0].lower().startswith("week") and parts[1].lower().startswith("week"):
                cleaned_line = f"{parts[0]}: {':'.join(parts[2:]).strip()}"
            else:
                cleaned_line = line
            cleaned.append(cleaned_line.strip())
        
        return cleaned


