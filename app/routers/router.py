from typing import Annotated

from fastapi import APIRouter, Depends

from app.repositories.repository import TaskRepository
from app.schemas.schemas import STaskAdd, STask, STaskId

tasks_router = APIRouter(
    prefix='/models',
    tags=['Таски']
)


@tasks_router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@tasks_router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
