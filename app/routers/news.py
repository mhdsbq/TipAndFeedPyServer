from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from ..services import get_news_service
from ..services.news import NewsService
from ..models.news import CreateNews, News, UpdateNews


router = APIRouter(
    prefix="/news",
)


@router.get("/")
async def get_news(
    news_service: Annotated[NewsService, Depends(get_news_service)],
) -> list[News]:
    return news_service.get_news()


@router.post("/")
async def create_news(
    create_news: CreateNews,
    news_service: Annotated[NewsService, Depends(get_news_service)],
) -> News:
    return news_service.create_news(create_news)


@router.get("/{id}")
async def get_news_by_id(
    id: int,
    news_service: Annotated[NewsService, Depends(get_news_service)],
) -> News:
    news = news_service.get_news_by_id(id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news


@router.delete("/{id}")
async def delete_news(
    id: int,
    news_service: Annotated[NewsService, Depends(get_news_service)],
) -> None:
    news_service.delete_news(id)


@router.patch("/{id}")
async def update_news(
    id: int,
    update_news: UpdateNews,
    news_service: Annotated[NewsService, Depends(get_news_service)],
) -> News:
    news = news_service.update_news(id, update_news)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news
