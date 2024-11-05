from fastapi import Depends

from ..database.database import get_db
from ..repository.news import NewsRepository


def get_news_repository(db=Depends(get_db)) -> NewsRepository:
    return NewsRepository(db)
