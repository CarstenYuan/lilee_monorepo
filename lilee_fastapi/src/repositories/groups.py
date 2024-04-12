import random
from sqlalchemy.orm import Session
from repositories.models.users_model import Users
from repositories.models.groups_model import Groups


class GroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_group(self, group_data: dict) -> Groups:
        new_group = Groups(**group_data)
        self.db.add(new_group)
        self.db.commit()
        self.db.refresh(new_group)
        return new_group
    