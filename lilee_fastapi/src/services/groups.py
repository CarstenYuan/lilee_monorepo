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