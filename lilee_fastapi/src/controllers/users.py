from fastapi import APIRouter, Depends, Body, Query
from pydantic import BaseModel, Field
from typing import Optional

from services.user_service import UserService
from dependencies import get_user_service


users_statistic_router = APIRouter()
users_tag = ['Users APIs']


class AddUserRequest(BaseModel):
    name: str = Field(..., description="The new name of the user.")
    group_id: Optional[int] = Field(None, description="The new group ID of the user.")


class UpdateUserInfoRequest(BaseModel):
    name: str = Field(None, description="The updated name of the user.")
    group_id: Optional[int] = Field(None, description="The updated group ID of the user.")
    is_activate: bool = Field(None, description="The updated activation status of the user.")


@users_statistic_router.post("/addUser", tags=users_tag)
def add_user(add_user_request: AddUserRequest = Body(...), service: UserService=Depends(get_user_service)):
    return service.add_user(add_user_request)


@users_statistic_router.delete("/deleteUser/{id}", tags=users_tag)
def delete_user(id, service: UserService=Depends(get_user_service)):
    return service.delete_user(id)


@users_statistic_router.get("/getSingleUser/{id}", tags=users_tag)
def get_single_user(id, service: UserService=Depends(get_user_service)):
     return service.get_single_user(id)


@users_statistic_router.get("/getAllUsers", tags=users_tag)
def get_all_users(filter: Optional[str] = Query(None), service: UserService=Depends(get_user_service)):
    return service.get_all_users(filter)


@users_statistic_router.patch("/updateIsUserActivate/{id}", tags=users_tag)
def update_is_activate(id: int, is_activate: bool, service: UserService=Depends(get_user_service)):
    return service.update_is_activate(id, is_activate)


@users_statistic_router.put("/updateUserInfo/{id}", tags=users_tag)
def update_user_info(id: int, update_request: UpdateUserInfoRequest = Body(...), service: UserService=Depends(get_user_service)):
    return service.update_user_info(id, update_request)
