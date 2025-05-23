from fastapi import FastAPI
from app.api.v1 import tasks
from app.db import database
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan, title="Todo API", version="1.0.0")
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])

origins = ["http://localhost:3000"]  # Replace with your frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

