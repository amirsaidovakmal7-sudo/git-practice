from fastapi import APIRouter, Depends
from schemas.user import UserResponse
from core.dependencies import get_current_user
from models.user import User

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/me", response_model=UserResponse)
async def get_current_user_api(user: User = Depends(get_current_user)):
    return user
