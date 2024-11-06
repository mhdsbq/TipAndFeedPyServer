from pydantic import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    class Config:
        env_file = ".env"
