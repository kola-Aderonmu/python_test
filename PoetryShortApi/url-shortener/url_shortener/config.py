# url_shortener/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str = "http://localhost:8000"
    database_url: str = "sqlite:///./shortener.db"


Settings = Settings()    