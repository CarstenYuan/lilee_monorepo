from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel, Field
from typing import Optional

from app.services.user_service import UserService
from app.dependencies import get_user_service


users_statistic_router = APIRouter()
users_tag = ['Users APIs']


class AddUserRequest(BaseModel):
    name: str = Field(..., description="The new name of the user.")
    group_id: Optional[int] = Field(None, description="The new group ID of the user.")


@users_statistic_router.post("/addUser", tags=users_tag)
def add_user(add_user_request: AddUserRequest = Body(...), service: UserService=Depends(get_user_service)):
    user = service.add_user(add_user_request)
    return user
