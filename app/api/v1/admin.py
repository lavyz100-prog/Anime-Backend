import uuid
from typing import List

from fastapi import APIRouter, Depends, status

from app.core.dependencies.user import get_user_service
from app.modules.User.schema import AdminResponse
from app.modules.User.service import UserService

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get(
    "/users", response_model=List[AdminResponse], status_code=status.HTTP_200_OK
)
async def get_all(service: UserService = Depends(get_user_service)):
    return await service.get_all()


@router.get(
    "/users/email", response_model=AdminResponse, status_code=status.HTTP_200_OK
)
async def get_all_admins(email: str, service: UserService = Depends(get_user_service)):
    return await service.get_user_by_email(email)


@router.get("/users/{user_id}", response_model=AdminResponse)
async def get_user(
    user_id: uuid.UUID, service: UserService = Depends(get_user_service)
):
    return await service.get_user(user_id)


@router.delete(
    "/users/{user_id}", response_model=AdminResponse, status_code=status.HTTP_200_OK
)
async def delete_user(
    user_id: uuid.UUID, service: UserService = Depends(get_user_service)
):
    return await service.delete_user(user_id)
