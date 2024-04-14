from pydantic import BaseModel
from fastapi import HTTPException
from repositories.users import UserRepository
from repositories.groups import GroupRepository
from repositories.models.users_model import Users


class UserService:
    def __init__(
        self, user_repository: UserRepository, group_repository: GroupRepository
    ):
        self.user_repository = user_repository
        self.group_repository = group_repository

    def add_user(self, user_data: BaseModel) -> Users:
        user_dict = user_data.dict()
        group_id = user_dict["group_id"]

        if group_id == 0:
            user_dict["group_id"] = None
        if group_id:
            group = self.group_repository.get_single_group(group_id)
            if not group:
                raise HTTPException(
                    status_code=404, detail=f"Group with id {group_id} does not exist."
                )
            elif group.is_activate != 1:
                raise HTTPException(
                    status_code=400, detail="You cannot join a deactivated group."
                )

        return self.user_repository.add_user(user_dict)

    def delete_user(self, id):
        if not self.user_repository.get_single_user(id):
            raise HTTPException(
                status_code=404, detail=f"User with id {id} does not exist."
            )
        return self.user_repository.delete_user(id)

    def get_single_user(self, id):
        user = self.user_repository.get_single_user(id)
        if user:
            return user
        raise HTTPException(
            status_code=404, detail=f"User with id {id} does not exist."
        )

    def get_users(self, username_filter):
        users = self.user_repository.get_users(username_filter)
        users_list = []
        for user in users:
            curr_id = user.id

            curr_name = user.name
            curr_group_id = user.group_id
            if curr_group_id:
                group = self.group_repository.get_single_group(curr_group_id)
                curr_group_name = group.name
            else:
                curr_group_name = None

            curr_creator = user.creator
            curr_createdTime = user.createdTime
            curr_modifier = user.modifier
            curr_modifiedTime = user.modifiedTime
            curr_is_activate = user.is_activate

            users_list.append(
                {
                    "id": curr_id,
                    "name": curr_name,
                    "group_id": curr_group_id,
                    "group": curr_group_name,
                    "creator": curr_creator,
                    "createdTime": curr_createdTime,
                    "modifier": curr_modifier,
                    "modifiedTime": curr_modifiedTime,
                    "is_activate": curr_is_activate,
                }
            )
        return users_list

    def update_user(self, id, update_data: BaseModel):
        update_dict = update_data.dict()
        group_id = update_dict["group_id"]
        user = self.user_repository.get_single_user(id)

        if not user:
            raise HTTPException(
                status_code=404, detail=f"User with id {id} does not exist."
            )
        if group_id == 0:
            update_dict["group_id"] = None
        if group_id:
            group = self.group_repository.get_single_group(group_id)
            if not group:
                raise HTTPException(
                    status_code=404, detail=f"Group with id {group_id} does not exist."
                )
            elif group.is_activate != 1:
                raise HTTPException(
                    status_code=400, detail="You cannot join a deactivated group."
                )

        has_changes = False
        for column, new_value in update_dict.items():
            if getattr(user, column) != new_value:
                has_changes = True
                break
        if has_changes:
            return self.user_repository.update_user(id, update_dict)
        return None
