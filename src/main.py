from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GetResponse(BaseModel):
    Hello: str

    @classmethod
    def res(cls) -> 'GetResponse':
        r = cls(Hello="World")
        return r


@app.get("/")
def read_root() -> GetResponse:
    return GetResponse.res()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
