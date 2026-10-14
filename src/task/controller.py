# All the logics are defined in the controller & connect it with the router
from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException


# create task
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
    return new_task


# get all the task
def get_tasks(db: Session):
    return db.query(TaskModel).all()


# get task by ID
def get_one_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="ID is incorrect")

    return one_task


# update the task
def update_task(body: TaskSchema, task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="ID is incorrect")

    body_dict = body.model_dump()
    for field, value in body_dict.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task


# delete the task
def delete_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="ID is incorrect")

    db.delete(one_task)
    db.commit()

    return None
