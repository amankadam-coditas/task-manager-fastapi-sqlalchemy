from pydantic import BaseModel
from typing import Optional, List
from ..models.enums import TaskPriority

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[TaskPriority] = TaskPriority.LOW

class TaskCreate(TaskBase):
    user_id: int

class TaskUpdateStatus(BaseModel):
    status: str

class Task(TaskBase):
    id: int
    status: str
    user_id: int
    class Config:
        orm_mode = True