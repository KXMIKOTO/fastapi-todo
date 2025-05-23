from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[StatusEnum] = StatusEnum.new
    priority: Optional[PriorityEnum] = PriorityEnum.medium
    deadline: Optional[datetime] = None
    category: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[StatusEnum]
    priority: Optional[PriorityEnum]
    deadline: Optional[datetime]
    category: Optional[str]

class TaskOut(TaskBase):
    id: int

    class Config:
        from_attributes = True  # важно для работы с ORM объектами
