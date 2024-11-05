from fastapi import FastAPI

from .routers import router
from .database.schema import Base
from .database.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
