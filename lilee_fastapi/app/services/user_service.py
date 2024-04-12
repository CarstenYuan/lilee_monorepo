from repositories.user_repository import UserRepository
from repositories.models.users_model import Users
from pydantic import BaseModel


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: BaseModel) -> Users:
        user_dict = user_data.dict()
        return self.user_repository.add_user(user_dict)
