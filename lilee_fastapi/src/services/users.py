from pydantic import BaseModel
from fastapi import HTTPException
from repositories.users import UserRepository
from repositories.models.users_model import Users



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

    def delete_user(self, id):
        if self.user_repository.get_single_user(id):
            return self.user_repository.delete_user(id)
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")
    
    def get_single_user(self, id):
        user = self.user_repository.get_single_user(id)
        if user:
            return user
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")
    
    def get_all_users(self, filter):
        return self.user_repository.get_all_users(filter=filter)

    def update_is_activate(self, id, is_activate):
        user = self.user_repository.update_activate_status(id, is_activate)
        if user:
            return user
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")

    def update_info(self, id, update_data: BaseModel):
        update_dict = update_data.dict()
        group_id = update_dict['group_id']

        if group_id == 0:
            update_dict['group_id'] = None
        if group_id and not (self.is_group_activated(group_id)):
            raise HTTPException(status_code=400, detail="You cannot join a deactivated group.")
        
        user = self.user_repository.update_user_info(id, update_dict)
        if user:
            return user
        raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")