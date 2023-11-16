from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.database import get_database
from src.user.auth_service import AuthService
from src.user.models.user_model import UserModel
from src.user.schemas.login_schema import LoginRequest, UserResponse
from src.user.user_service import UserService


router = APIRouter()


@router.post('/register', response_model=UserResponse)
def register(
    new_user_request: LoginRequest,
    database: Annotated[Session, Depends(get_database)],
    user_service: Annotated[UserService, Depends(UserService.instantiate)],
) -> Any:
    existing = database.query(UserModel).filter(
        UserModel.username == new_user_request.username).first()
    if existing is not None:
        raise HTTPException(
            status_code=400, detail="Username has already been registered")
    new_user = user_service.create_user_model(new_user_request)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


@router.post('/login', response_model=UserResponse)
def login(
    login_request: LoginRequest,
    database: Annotated[Session, Depends(get_database)],
    auth_service: Annotated[AuthService, Depends(AuthService.instantiate)],
) -> Any:
    user = database.query(UserModel).filter(
        UserModel.username == login_request.username).first()
    if user is None:
        raise HTTPException(400, 'Invalid Login')
    hashed_password = user.password
    is_valid = auth_service.verify_password(
        login_request.password, hashed_password)
    if not is_valid:
        raise HTTPException(400, 'Invalid Login')
    return user
