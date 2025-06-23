from typing import Literal

from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    name: str = Field(max_length=40, min_length=3)
    age: int = Field(ge=14)
    sex: Literal["male", "female"]
    description: str = Field(max_length=300)
    games: list[str] = []
