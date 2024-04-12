from fastapi import Depends
from sqlalchemy.orm import Session
from common.database import get_db
from repositories.users import UserRepository
from services.users import UserService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)
