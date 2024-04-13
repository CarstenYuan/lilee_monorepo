from fastapi import Depends
from sqlalchemy.orm import Session
from common.database import get_session
from repositories.users import UserRepository
from repositories.groups import GroupRepository
from services.users import UserService
from services.groups import GroupService

def get_user_service(db: Session = Depends(get_session)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)

def get_group_service(db: Session = Depends(get_session)) -> GroupService:
    group_repository = GroupRepository(db)
    return GroupService(group_repository)