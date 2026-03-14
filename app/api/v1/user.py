import uuid

from fastapi import APIRouter, Depends, status

from app.core.dependencies.user import get_user_service
from app.modules.User.schema import UserCreate, UserResponse, UserUpdate
from app.modules.User.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserCreate, service: UserService = Depends(get_user_service)
):
    return await service.create_user(data)


@router.patch(
    "/{user_id}", response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED
)
async def update_user(
    user_id: uuid.UUID,
    data: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    return await service.update_user(user_id, data)
