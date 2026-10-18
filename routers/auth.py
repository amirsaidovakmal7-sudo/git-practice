from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user import CreateUser, UserResponse
from schemas.token import Token
from core.config import settings
from core.security import verify_password, create_access_token, create_refresh_token, decode_token
from services.user import get_user_filter, create_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
async def register_user(user_data: CreateUser):
    existing_user = await get_user_filter(user_data.username, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username or email already exists", headers={"WWW-Authenticate": "Bearer"})
    new_user = await create_user(user_data)
    return new_user

@router.post("/login", response_model=Token)
async def login_api(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_filter(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token = create_access_token(data={"sub": user.user_id})
    refresh_token = create_refresh_token(data={"sub": user.user_id})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.put("/refresh", response_model=Token)
async def refresh_token_api(refresh_token: str):
    payload = decode_token(refresh_token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid refresh token",
                            headers={"WWW-Authenticate": "Bearer"})
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid refresh token",
                            headers={"WWW-Authenticate": "Bearer"})
    new_access_token = create_access_token(data={"user_id": user_id})

    return {"access_token": new_access_token, "refresh_token": refresh_token, "token_type": "bearer"}


