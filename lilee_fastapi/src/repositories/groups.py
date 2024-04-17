import random
from sqlalchemy.orm import Session
from .models.groups_model import Groups


class GroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_group(self, group_data: dict) -> Groups:
        new_group = Groups(**group_data)
        new_group.creator = random.choice(
            ["Admin", "Jay Chou", "Eason Chen", "Carsten Yuan"]
        )
        self.db.add(new_group)
        self.db.commit()
        self.db.refresh(new_group)
        return new_group

    def delete_group(self, group_id):
        group = self.get_single_group(group_id)
        self.db.delete(group)
        self.db.commit()
        return group

    def get_single_group(self, group_id):
        return self.db.query(Groups).filter(Groups.id == group_id).one_or_none()

    def get_groups(self, activated_only):
        if activated_only:
            return self.db.query(Groups).filter(Groups.is_activate == 1).all()
        return self.db.query(Groups).all()

    def update_group(self, group_id, update_data: dict):
        group = self.get_single_group(group_id)
        group.name = update_data["name"]
        group.is_activate = update_data["is_activate"]
        group.modifier = random.choice(
            ["Alice", "Bob", "Charlie", "David", "Eve"]
        )  # Mock modifiers
        self.db.commit()
        return group
