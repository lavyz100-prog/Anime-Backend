from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

DB_URL = f"postgresql+asyncpg://{settings.USERNAME}:{settings.PASSWORD}@localhost/{settings.DBNAME}"

engine = create_async_engine(DB_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
