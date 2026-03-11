from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .config import settings

# No username/password needed, just the file name
DATABASE_URL = settings.DB_URL

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
