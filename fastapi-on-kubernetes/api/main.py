import sys
import os
import signal
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Kubernetes Experimentation", version="1.0")


@app.get("/")
async def home():
    return {"status": "successful", "message": "FastAPI on Kubernetes"}


@app.get("/error")
async def error():
    os.kill(os.getpid(), signal.SIGTERM)

@app.get("/services")
async def get_services():
    return JSONResponse({}, status_code=200)
