import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.models.database import create_tables, delete_tables
from app.routers.router import tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
server = uvicorn.Server(config=uvicorn.Config(app))

loop = asyncio.get_event_loop()
loop.run_until_complete(server.serve())
