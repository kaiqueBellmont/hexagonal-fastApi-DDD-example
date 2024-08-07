import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../configurator/.env")
load_dotenv(dotenv_path)


class Settings(BaseSettings):

    PROJECT_NAME: str = "WYD backend"
    PROJECT_VERSION: str = "1.0.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    ALGORITHM: str = os.getenv("ALGORITHM")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()
