import sys
import os
import signal
from fastapi import FastAPI

app = FastAPI(title="Kubernetes Experimentation", version="1.0")


@app.get("/")
async def home():
    return {"status": "successful", "message": "FastAPI on Kubernetes"}


@app.get("/error")
async def error():
    os.kill(os.getpid(), signal.SIGTERM)
