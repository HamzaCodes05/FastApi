# All the logics are defined in the controller & connect it with the router
from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException


def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status": "Task Created Successfully", "data": new_task}


def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"status": "All tasks", "data": tasks}


def get_one_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="ID is incorrect")

    return {"status": "Task Fethced successfully", "data": one_task}
