from fastapi import APIRouter, Depends, Body, Query
from pydantic import BaseModel, Field
from typing import Optional

from services.groups import GroupService
from common.dependencies import get_group_service


groups_statistic_router = APIRouter()
groups_tag = ["Groups APIs"]


class AddGroupRequest(BaseModel):
    name: str = Field(description="The new name of the group.")


@groups_statistic_router.post("/addGroup", tags=groups_tag)
def add_group(
    add_request: AddGroupRequest = Body(...),
    service: GroupService = Depends(get_group_service),
):
    return service.add_group(add_request)
