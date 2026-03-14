# crud/service.py
import uuid
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password

from .model import User
from .repository import UserRepository
from .schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def create_user(self, data: UserCreate) -> User:
        existing = await self.repo.get_by_email(data.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email already registered"
            )
        data.password = hash_password(data.password)
        return await self.repo.create(data)

    async def get_all(self) -> List[User]:
        users = await self.repo.get_all()
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users

    async def get_user(self, user_id: uuid.UUID) -> User:
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found",
            )
        return user

    async def get_user_by_email(self, email: str) -> User:
        user = await self.repo.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email '{email}' not found",
            )
        return user

    async def update_user(self, user_id: uuid.UUID, data: UserUpdate) -> User:
        # check if new email is taken by another user
        if data.email:
            existing = await self.repo.get_by_email(data.email)
            if existing and existing.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="Email already in use"
                )
        user = await self.repo.update(user_id, **data.model_dump(exclude_none=True))
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found",
            )
        return user

    async def delete_user(self, user_id: uuid.UUID) -> User:
        user = await self.repo.delete(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found",
            )
        return user
