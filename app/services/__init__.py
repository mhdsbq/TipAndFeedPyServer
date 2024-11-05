from typing import Annotated
from fastapi import Depends

from ..repository import get_news_repository
from ..repository.news import NewsRepository
from ..services.news import NewsService


def get_news_service(
    repository: Annotated[NewsRepository, Depends(get_news_repository)]
) -> NewsService:
    return NewsService(repository)
