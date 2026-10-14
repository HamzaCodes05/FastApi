from typing import List

from fastapi import APIRouter, Depends, status

from src.task import controller
from src.task.dtos import TaskResponseSchema, TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/tasks")


# Creates the task
@task_routes.post(
    "/create",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


# Get all the tasks
@task_routes.get(
    "/all_tasks",
    response_model=List[TaskResponseSchema],
    status_code=status.HTTP_200_OK,
)
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)


# Get task by id
@task_routes.get(
    "/one_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)


# update task
@task_routes.put(
    "/update_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def update_task(body: TaskSchema, task_id: int, db: Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)


# delete task
@task_routes.delete(
    "/delete_task/{task_id}",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)
