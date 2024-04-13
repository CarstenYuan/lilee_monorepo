import random
from sqlalchemy.orm import Session
from repositories.models.users_model import Users
from repositories.models.groups_model import Groups


class GroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_group(self, group_data: dict) -> Groups:
        new_group = Groups(**group_data)
        new_group.creator = random.choice(["Admin", "Jay Chou", "Eason Chen", "Carsten Yuan"])
        self.db.add(new_group)
        self.db.commit()
        self.db.refresh(new_group)
        return new_group

    def delete_group(self, id):
        group = self.get_single_group(id)
        self.db.delete(group)
        self.db.commit()
        return group

    def has_member(self, id) -> bool:
        return self.db.query(Users).filter(Users.group_id == id).count() != 0

    def get_single_group(self, id):
        return self.db.query(Groups).filter(Groups.id == id).one_or_none()

    def get_all_groups(self):
        return self.db.query(Groups).all()

    def get_active_group(self):
        return self.db.query(Groups).filter(Groups.is_activate == 1).all()

    def update_activate_status(self, id, is_activate):
        group = self.get_single_group(id)
        group.is_activate = is_activate
        group.modifier = random.choice(
            ["Alice", "Bob", "Charlie", "David", "Eve"]
        )  # Mock modifiers
        self.db.commit()
        return group

    def update_info(self, id, update_data: dict):
        group = self.get_single_group(id)
        group.name = update_data["name"]
        group.is_activate = update_data["is_activate"]
        group.modifier = random.choice(
            ["Alice", "Bob", "Charlie", "David", "Eve"]
        )  # Mock modifiers
        self.db.commit()
        return group
