from fastapi import APIRouter

from .news import router as newsRouter

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

router.include_router(newsRouter)
