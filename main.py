from fastapi import FastAPI
from schemas import *

app = FastAPI()

@app.get("/")
def home_get():
    return "hello world from get!"


@app.post("/")
def home_post() -> OutputSchema:
    return {
        "msg": "hello world from post!"
    }


@app.put("/")
def home_put():
    return "hello world from put!"


@app.delete("/")
def home_del():
    return "hello world from delete!"