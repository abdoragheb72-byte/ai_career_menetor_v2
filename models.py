from pydantic import BaseModel, Field


class CVEvaluation(BaseModel):
    user_id: int
    cv_text: str
    score: float = Field(ge=0, le=100)
    feedback: str
    date: str