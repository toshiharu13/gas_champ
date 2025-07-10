from fastapi import FastAPI, Path, Query
from typing import Annotated

from .routers import ml_model

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

app.include_router(ml_model.router)