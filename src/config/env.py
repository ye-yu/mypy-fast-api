import os
from pydantic import BaseModel, Field


class Env(BaseModel):
    APP_NAME: str = Field(default="")
    APP_SECRET: str

    def __init__(self):
        BaseModel.__init__(self, **os.environ)
