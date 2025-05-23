from fastapi import FastAPI
from app.api.v1 import tasks

app = FastAPI(title="ToDo Project", version="1.0.0")

app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])