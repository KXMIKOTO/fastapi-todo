from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.models.models.task import Task as TaskModel
from app.db import database, engine
from app.db import Base


Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])

@router.post("/", response_model=TaskOut)
async def create_task(task: TaskCreate):
    query = TaskModel.__table__.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), "id": last_record_id}

@router.get("/", response_model=List[TaskOut])
async def list_tasks():
    query = TaskModel.__table__.select()
    return await database.fetch_all(query)

@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: int):
    query = TaskModel.__table__.select().where(TaskModel.id == task_id)
    task = await database.fetch_one(query)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: int, task_update: TaskUpdate):
    query = TaskModel.__table__.update().where(TaskModel.id == task_id).values(**task_update.model_dump(exclude_unset=True))
    await database.execute(query)
    query = TaskModel.__table__.select().where(TaskModel.id == task_id)
    task = await database.fetch_one(query)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int):
    query = TaskModel.__table__.delete().where(TaskModel.id == task_id)
    await database.execute(query)