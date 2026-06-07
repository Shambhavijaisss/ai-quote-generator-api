from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    REDIS_URL: str
    CACHE_TTL: int = 3600

    class Config:
        env_file = ".env"


settings = Settings()