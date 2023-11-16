import os
from pydantic import BaseModel, ConfigDict, Field


class Env(BaseModel):
    APP_NAME: str = Field(default="")
    APP_SECRET: str

    model_config = ConfigDict(hide_input_in_errors=True)

    def __init__(self):
        BaseModel.__init__(self, **os.environ)
