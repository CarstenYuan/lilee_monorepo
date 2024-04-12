import random
from sqlalchemy.orm import Session
from repositories.models.users_model import Users
from repositories.models.groups_model import Groups


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

    def delete_user(self, id):
        user = self.get_single_user_by_id(id)
        self.db.delete(user)
        self.db.commit()
        return user

    def get_single_user_by_id(self, id):
        return self.db.query(Users).filter(Users.id == id).one_or_none()
    
    def get_all_users(self, filter: str = None):
        query = self.db.query(Users)
        if filter:
            query = query.filter(Users.name.like(f"%{filter}%"))
        return query.all()

    def update_activate_status(self, id, is_activate):
        user = self.get_single_user_by_id(id)
        if user:
            user.is_activate = is_activate
            user.modifier = random.choice(["Alice", "Bob", "Charlie", "David", "Eve"])  # Mock modifiers
            self.db.commit()
            return user
        return None
    
    def update_user_info(self, id, update_data: dict):
        user = self.get_single_user_by_id(id)
        if user:
            has_changes = False

            for key, new_value in update_data.items():
                if getattr(user, key) != new_value:
                    setattr(user, key, new_value)
                    has_changes = True
            if has_changes:
                modifier = random.choice(["Alice", "Bob", "Charlie", "David", "Eve"])  # Mock modifiers
                user.modifier = modifier
                self.db.commit()
            else:
                self.db.rollback()
            return user
        return None
