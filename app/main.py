from fastapi import FastAPI
from pydantic import BaseModel
from .handler import init_app


app = FastAPI()
init_app(app)


class User(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(user: User):
    return {"message": "login"}
