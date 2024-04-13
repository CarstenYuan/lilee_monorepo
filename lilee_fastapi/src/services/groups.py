from pydantic import BaseModel
from fastapi import HTTPException
from repositories.groups import GroupRepository
from repositories.models.groups_model import Groups


class GroupService:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def add_group(self, group_data: BaseModel) -> Groups:
        group_dict = group_data.dict()
        return self.group_repository.add_group(group_dict)

    def delete_group(self, id):
        if not self.group_repository.get_single_group(id):
            raise HTTPException(status_code=404, detail=f"Group with id {id} does not exist.")
        if self.has_member(id):
            raise HTTPException(status_code=400, detail="Group cannot be deleted because it has members.")
        return self.group_repository.delete_group(id)
        
    def has_member(self, id):
        return self.group_repository.has_member(id)

    def get_single_group(self, id):
        group = self.group_repository.get_single_group(id)
        if group:
            return group
        raise HTTPException(status_code=404, detail=f"Group with id {id} does not exist.")

    def get_all_groups(self):
        return self.group_repository.get_all_groups()

    def get_active_group(self):
        pass

    def update_is_activate(self, id, is_activate):
        pass

    def update_info(self, id, update_data: BaseModel):
        pass
