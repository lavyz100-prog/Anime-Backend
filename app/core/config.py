from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USERNAME: str = "alpha"
    PASSWORD: str = "jack2312"
    DBNAME: str = "evodb"


settings = Settings()
