from pydantic import BaseModel
from fastapi import HTTPException
from repositories.groups import GroupRepository
from repositories.models.groups_model import Groups


class GroupService:
    def __init__(self, group_repository: GroupRepository, user_service):
        self.group_repository = group_repository
        self.user_service = user_service

    def add_group(self, group_data: BaseModel) -> Groups:
        group_dict = group_data.dict()
        return self.group_repository.add_group(group_dict)

    def delete_group(self, id):
        if not self.group_repository.get_single_group(id):
            raise HTTPException(
                status_code=404, detail=f"Group with id {id} does not exist."
            )
        if self.user_service.has_user(id):
            raise HTTPException(
                status_code=400,
                detail="Group cannot be deleted because it has members.",
            )
        return self.group_repository.delete_group(id)

    def get_single_group(self, id):
        group = self.group_repository.get_single_group(id)
        if group:
            return group
        raise HTTPException(
            status_code=404, detail=f"Group with id {id} does not exist."
        )

    def get_groups(self, activated_only=False):
        return self.group_repository.get_groups(activated_only)

    def update_group(self, id, update_data: BaseModel):
        update_dict = update_data.dict()
        group = self.group_repository.get_single_group(id)

        if not group:
            raise HTTPException(
                status_code=404, detail=f"Group with id {id} does not exist."
            )
        if (not update_dict["is_activate"]) and self.user_service.has_user(id):
            raise HTTPException(
                status_code=400,
                detail="Group cannot be deactivated because it has members.",
            )

        has_changes = False
        for column, new_value in update_dict.items():
            if getattr(group, column) != new_value:
                has_changes = True
                break
        if has_changes:
            return self.group_repository.update_group(id, update_dict)
        return None

    def is_group_activated(self, id) -> bool:
        group = self.get_single_group(id)
        return group.is_activate == 1
