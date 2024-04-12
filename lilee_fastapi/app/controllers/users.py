from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel, Field
from typing import Optional

from services.user_service import UserService  # 確保已經有此服務層實現
from dependencies import get_user_service  # 依賴注入的方法，需實現


users_statistic_router = APIRouter()
users_tag = ['Users APIs']


class AddUserRequest(BaseModel):
    name: str = Field(..., description="The new name of the user.")
    group_id: Optional[int] = Field(None, description="The new group ID of the user.")


# class UpdateUserInfoRequest(BaseModel):
#     name: str = Field(None, description="The updated name of the user.")
#     group_id: Optional[int] = Field(None, description="The updated group ID of the user.")
#     is_activate: bool = Field(None, description="The updated activation status of the user.")


@users_statistic_router.post("/addUser", tags=users_tag)
def add_user(add_user_request: AddUserRequest = Body(...), service: UserService = Depends(get_user_service)):
    try:
        user = service.create_user(add_user_request)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# @users_statistic_router.delete("/deleteUser/{id}", tags=users_tag)
# def delete_user(id: int):
#     user = delete_item(Users, id)
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")


# @users_statistic_router.get("/getSingleUser/{id}", tags=users_tag)
# def get_single_user(id: int):
#     user = get_single_item(Users, id)
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")


# @users_statistic_router.get("/getAllUsers", tags=users_tag)
# def get_all_users(filter: Optional[str] = Query(None)):
#     users = get_all_items(Users, filter=filter)
#     users_list = []
#     for user in users:
#         curr_id = user.id

#         curr_name = user.name
#         curr_group_id = user.group_id
#         group = get_single_item(Groups, curr_group_id)
#         curr_group_name = group.name if group else None

#         curr_creator = user.creator
#         curr_createdTime = user.createdTime
#         curr_modifier = user.modifier
#         curr_modifiedTime = user.modifiedTime
#         curr_is_activate = user.is_activate

#         users_list.append(
#             {
#             'id': curr_id,
#             'name': curr_name,
#             'group_id': curr_group_id,
#             'group': curr_group_name,

#             'creator': curr_creator,
#             'createdTime': curr_createdTime,
#             'modifier': curr_modifier,
#             'modifiedTime': curr_modifiedTime,
#             'is_activate': curr_is_activate
#             }
#         )
#     return users_list


# @users_statistic_router.patch("/updateIsUserActivate/{id}", tags=users_tag)
# def update_is_user_activate(id: int, is_activate: bool):
#     user = update_is_activate(Users, id, is_activate)
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")


# @users_statistic_router.put("/updateUserInfo/{id}", tags=users_tag)
# def update_user_info(id: int, update_request: UpdateUserInfoRequest = Body(...)):
#     update_data = update_request.dict()
#     user = update_items(Users, id, update_data)
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail=f"User with id {id} does not exist.")
