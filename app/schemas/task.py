from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.models.task import StatusEnum, PriorityEnum

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.new
    priority: PriorityEnum = PriorityEnum.medium
    deadline: Optional[datetime] = None
    category: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[StatusEnum]
    priority: Optional[PriorityEnum]
    deadline: Optional[datetime]
    category: Optional[str]

class TaskOut(BaseModel):
    id: int