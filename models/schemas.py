from typing import Literal

from pydantic import BaseModel, Field


class ReviewFinding(BaseModel):
    severity: Literal["Critical", "High", "Medium", "Low", "Info"]
    category: str
    line_number: int | None = None
    description: str
    recommendation: str


class CodeReviewReport(BaseModel):
    filename: str
    review_mode: Literal["quick", "thorough", "security-focused"]
    overall_score: int = Field(ge=0, le=100)
    summary: str
    findings: list[ReviewFinding] = Field(default_factory=list)
    positive_aspects: list[str] = Field(default_factory=list)
