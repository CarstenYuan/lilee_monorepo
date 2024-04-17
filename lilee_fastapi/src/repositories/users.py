import random
from sqlalchemy.orm import Session
from ..repositories.models.users_model import Users


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_user(self, user_data: dict) -> Users:
        new_user = Users(**user_data)
        new_user.creator = random.choice(
            ["Admin", "Jay Chou", "Eason Chen", "Carsten Yuan"]
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def delete_user(self, user_id):
        user = self.get_single_user(user_id)
        self.db.delete(user)
        self.db.commit()
        return user

    def get_single_user(self, user_id):
        return self.db.query(Users).filter(Users.id == user_id).one_or_none()

    def get_users(self, username_filter: str = None):
        query = self.db.query(Users)
        if username_filter:
            query = query.filter(Users.name.like(f"%{username_filter}%"))
        return query.all()

    def update_user(self, user_id, update_data: dict):
        user = self.get_single_user(user_id)
        user.name = update_data["name"]
        user.group_id = update_data["group_id"]
        user.is_activate = update_data["is_activate"]
        user.modifier = random.choice(
            ["Alice", "Bob", "Charlie", "David", "Eve"]
        )  # Mock modifiers
        self.db.commit()
        return user

    def has_user(self, group_id) -> bool:
        return self.db.query(Users).filter(Users.group_id == group_id).count() != 0
