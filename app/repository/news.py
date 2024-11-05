from sqlalchemy.orm import Session

from ..database.schema import News


class NewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_news(self, news: News) -> News:
        self.db.add(news)
        self.db.commit()
        self.db.refresh(news)
        return news

    def get_news(self) -> list[News]:
        return self.db.query(News).all()

    def get_news_by_id(self, id: int) -> News | None:
        return self.db.query(News).filter(News.id == id).first()

    def delete_news(self, id: int) -> None:
        self.db.query(News).filter(News.id == id).delete()
        self.db.commit()

    def update_news(self, id: int, news: News) -> News | None:
        existing_news = self.db.query(News).filter(News.id == id).first()
        if not existing_news:
            return None

        if news.title:
            existing_news.title = news.title
        if news.body:
            existing_news.body = news.body
        if news.image_url:
            existing_news.image_url = news.image_url
        if news.source_url:
            existing_news.source_url = news.source_url

        self.db.commit()
        self.db.refresh(existing_news)
        return existing_news
