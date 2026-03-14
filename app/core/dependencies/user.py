# crud/dependency.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.User.service import UserService

from .db import get_db


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)
