from fastapi import FastAPI
from app.api.v1 import tasks
from app.db import database
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])