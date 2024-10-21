from sqlalchemy import select

from app.models.database import session_factory, TaskOrm
from app.schemas.schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with session_factory() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with session_factory() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [
                STask.model_validate(
                    task_model
                ) for task_model in task_models
            ]
            return task_schemas
