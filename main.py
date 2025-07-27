from fastapi import FastAPI, Path, Query

from routers import sensor
from routers import device

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

app.include_router(sensor.router)
app.include_router(device.router)