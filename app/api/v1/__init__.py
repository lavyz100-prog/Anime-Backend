from fastapi import APIRouter

from .admin import router as admin
from .user import router as user

app = APIRouter(prefix="/api/v1")

app.include_router(user)
app.include_router(admin)
