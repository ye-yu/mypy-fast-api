from typing import Union

from fastapi import Depends, FastAPI
from .main_service import GetResponse, MainService

app = FastAPI()


@app.get("/")
def read_root(service: MainService = Depends(MainService.instantiate)) -> GetResponse:
    return service.GetResponse()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
