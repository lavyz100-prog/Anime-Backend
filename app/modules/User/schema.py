# crud/schema.py
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.modules.User.model import Roles


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class AdminUpdate(UserUpdate):
    role: Optional[Roles] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}


class AdminResponse(UserResponse):
    role: Roles
    is_active: bool
    updated_at: datetime
