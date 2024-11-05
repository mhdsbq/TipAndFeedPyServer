from ..database import schema
from ..models.news import CreateNews, News, UpdateNews
from ..repository.news import NewsRepository


class NewsService:
    def __init__(self, repository: NewsRepository):
        self.repository = repository

    def create_news(self, create_news: CreateNews) -> News:
        news_schema = schema.News(**create_news.model_dump())
        news = self.repository.create_news(news_schema)
        return News(**news.__dict__)

    def get_news(self) -> list[News]:
        news = self.repository.get_news()
        return [News(**news.__dict__) for news in news]

    def get_news_by_id(self, id: int) -> News | None:
        news = self.repository.get_news_by_id(id)
        return News(**news.__dict__) if news else None

    def delete_news(self, id: int) -> None:
        self.repository.delete_news(id)

    def update_news(self, id: int, update_news: UpdateNews) -> News:
        news_schema = schema.News(**update_news.model_dump())
        news_schema.id = id
        news = self.repository.update_news(id, news_schema)
        return News(**news.__dict__) if news else None
