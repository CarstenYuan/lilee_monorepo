from sqlalchemy.orm import Session
from app.repositories.models.users_model import Users
from app.repositories.models.groups_model import Groups


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_user(self, user_data: dict) -> Users:
        new_user = Users(**user_data)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_single_group(self, group_id):
        return self.db.query(Groups).filter(Groups.id == group_id).one_or_none()
