
from pydantic import BaseModel, Field
from typing import Literal


class InterviewConfig(BaseModel):

    role: str = Field(
        min_length=2,
        description="Job role"
    )

    experience: Literal[
        "Fresher",
        "0-2 Years",
        "2-5 Years",
        "5+ Years"
    ]

    domain: str = Field(
        min_length=2,
        description="Technical domain"
    )

    difficulty: Literal[
        "Easy",
        "Medium",
        "Hard"
    ]

    number: int = Field(
        ge=1,
        le=20,
        description="Number of interview questions"
    )
