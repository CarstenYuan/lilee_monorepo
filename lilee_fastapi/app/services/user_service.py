from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.repositories.models.users_model import Users
from pydantic import BaseModel


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add_user(self, user_data: BaseModel) -> Users:
        user_dict = user_data.dict()
        group_id = user_dict['group_id']

        if group_id == 0:
            user_dict['group_id'] = None
        if group_id and not (self.is_group_activated(group_id)):
            raise HTTPException(status_code=400, detail="You cannot join a deactivated group.")
        
        return self.user_repository.add_user(user_dict)

    def is_group_activated(self, group_id):
        group = self.user_repository.get_single_group(group_id)
        if group:
            return group.is_activate
        raise HTTPException(status_code=404, detail=f"Group with id {group_id} does not exist.")
