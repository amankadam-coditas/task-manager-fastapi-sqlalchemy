
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schema import schemas
from .. import crud_task
from ..database import SessionLocal

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db, task)

@router.get("/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud_task.get_tasks(db)

@router.get("/user/{user_id}", response_model=list[schemas.Task])
def read_tasks_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud_task.get_tasks_by_user(db, user_id)

@router.patch("/{task_id}/status", response_model=schemas.Task)
def update_task_status(task_id: int, update: schemas.TaskUpdateStatus, db: Session = Depends(get_db)):
    task = crud_task.update_task_status(db, task_id, update.status)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if not crud_task.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
