from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task(task: TaskCreate):
    global task_id
    new_task = task.dict()
    new_task["id"] = task_id_seq
    task_id_seq += 1
    tasks.append(new_task)
    return new_task

@router.get("/", response_model=List[TaskOut])
async def list_tasks():
    return tasks


@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task.update(task_update.dict(exclude_unset=True))
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete_task("/{task_id}", status_code=204)
async def delete_task(task_id: int):
    global tasks
    tasks = [
        task for task in tasks if task["id"] != task_id
    ]