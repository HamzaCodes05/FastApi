from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")


# Creates the task
@task_routes.post("/create")
def create_task(body: TaskSchema, db=Depends(get_db)):
    print(body.model_dump())
    return controller.create_task(body, db)


# Get all the tasks
@task_routes.get("/all_tasks")
def get_all_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)


# Get task by id
@task_routes.get("/get_one/{task_id}")
def get_one(task_id: int, db=Depends(get_db)):
    return controller.get_one_task(task_id, db)
