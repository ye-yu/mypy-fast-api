from typing import Annotated

from fastapi import Depends
from src.user.auth_service import AuthService
from src.user.models.user_model import UserModel
from src.user.schemas.login_schema import LoginRequest


class UserService:
    auth_service: AuthService

    def create_user_model(self, register_body: LoginRequest) -> UserModel:
        hashed_password = self.auth_service.hash_password(
            register_body.password)
        user = UserModel(username=register_body.username,
                         password=hashed_password)
        return user

    @staticmethod
    def instantiate(
        auth_service: Annotated[AuthService, Depends(AuthService.instantiate)]
    ) -> 'UserService':
        i = UserService()
        i.auth_service = auth_service
        return i
