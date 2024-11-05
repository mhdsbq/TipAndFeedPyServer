from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    image_url = Column(String)
    source_url = Column(String)

    def __repr__(self):
        return f"<News(id={self.id}, title='{self.title}', body='{self.body}', image_url='{self.image_url}', source_url='{self.source_url}')>"
