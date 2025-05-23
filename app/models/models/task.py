from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.new
    priority: PriorityEnum = PriorityEnum.medium
    deadline: Optional[datetime] = None
    category: Optional[str] = None