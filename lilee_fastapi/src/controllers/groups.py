from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel, Field
from typing import Optional

from services.groups import GroupService
from common.dependencies import get_group_service


groups_statistic_router = APIRouter()
groups_tag = ["Groups APIs"]


# TODO: Move this class to controllers/models/groups_model.py
class AddGroupRequest(BaseModel):
    name: str = Field(description="The new name of the group.")


# TODO: Move this class to controllers/models/groups_model.py
class UpdateGroupRequest(BaseModel):
    name: Optional[str] = Field(None, description="The new name of the group.")
    is_activate: Optional[bool] = Field(
        None, description="The new activation status of the group."
    )


@groups_statistic_router.post("/addGroup", tags=groups_tag)
def add_group(
    add_request: AddGroupRequest = Body(...),
    service: GroupService = Depends(get_group_service),
):
    return service.add_group(add_request)


@groups_statistic_router.delete("/deleteGroup/{id}", tags=groups_tag)
def delete_group(id: int, service: GroupService = Depends(get_group_service)):
    return service.delete_group(id)


@groups_statistic_router.get("/getSingleGroup/{id}", tags=groups_tag)
def get_single_group(id: int, service: GroupService = Depends(get_group_service)):
    return service.get_single_group(id)


@groups_statistic_router.get("/getAllGroups", tags=groups_tag)
def get_all_groups(service: GroupService = Depends(get_group_service)):
    return service.get_groups()


@groups_statistic_router.get("/getActiveGroups", tags=groups_tag)
def get_active_groups(service: GroupService = Depends(get_group_service)):
    return service.get_groups(activated_only=True)


# TODO: modify api route here and vue's
@groups_statistic_router.put("/updateGroupInfo/{id}", tags=groups_tag)
def update_group(
    id: int,
    update_request: UpdateGroupRequest = Body(...),
    service: GroupService = Depends(get_group_service),
):
    return service.update_group(id, update_request)
