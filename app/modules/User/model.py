import uuid
from datetime import datetime
from enum import Enum as PEnum

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Roles(PEnum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )

    password: Mapped[str] = mapped_column(String(255), nullable=False)

    role: Mapped[Roles] = mapped_column(Enum(Roles), default=Roles.USER, nullable=False)

    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
