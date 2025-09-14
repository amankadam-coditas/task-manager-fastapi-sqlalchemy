from fastapi import FastAPI
from .database import Base, engine
from .services import user, task

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Manage users and tasks with FastAPI, SQLAlchemy, and SQLite",
    version="0.1.0"
)

app.include_router(user.router)
app.include_router(task.router)