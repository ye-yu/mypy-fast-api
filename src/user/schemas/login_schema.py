from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class LoginRequest(BaseModel):
    username: str = Field(min_length=6, max_length=50, examples=["username"])
    password: str = Field(min_length=10, max_length=50,
                          examples=["password11"])

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    username: str
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)
