# crud/repository.py
import uuid
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User
from .schema import UserCreate


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: UserCreate) -> User:
        user = User(username=data.username, email=data.email, password=data.password)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_all(self) -> List[User]:
        result = await self.db.execute(select(User))
        return list(result.scalars().all())

    async def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def update(self, user_id: uuid.UUID, **kwargs) -> Optional[User]:
        user = await self.get_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, user_id: uuid.UUID) -> Optional[User]:
        user = await self.get_by_id(user_id)
        if user:
            user.is_active = False  # SQLAlchemy tracks this change automatically
            await self.db.commit()
            await self.db.refresh(user)
        else:
            return None
        return user
