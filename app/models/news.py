from pydantic import BaseModel


class News(BaseModel):
    id: int
    title: str
    body: str
    image_url: str
    source_url: str


class CreateNews(BaseModel):
    title: str
    body: str
    image_url: str
    source_url: str


class UpdateNews(BaseModel):
    title: str | None
    body: str | None
    image_url: str | None
    source_url: str | None
