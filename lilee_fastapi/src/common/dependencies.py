from fastapi import Depends
from sqlalchemy.orm import Session
from common.database import get_session
from repositories.users import UserRepository
from repositories.groups import GroupRepository
from services.users import UserService
from services.groups import GroupService


def get_group_service(db: Session = Depends(get_session)) -> GroupService:
    group_repository = GroupRepository(db)
    user_repository = UserRepository(db)
    user_service = user_repository
    return GroupService(group_repository, user_service)


def get_user_service(
    db: Session = Depends(get_session),
    group_service: GroupService = Depends(get_group_service),
) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository, group_service)
