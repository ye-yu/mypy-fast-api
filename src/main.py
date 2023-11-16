from fastapi import FastAPI

from src.user import user_controller


app = FastAPI()

app.include_router(user_controller.router, prefix="/users", tags=["users"])
