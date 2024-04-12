import os
import sys
import json
import random


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from src.repositories.models.base import Base
from src.repositories.models.groups_model import Groups
from src.repositories.models.users_model import Users
from src.repositories.database import SessionLocal


def populate_data(db, data):
    creators = ["root", "carsten"]

    for group in data["groups"]:
        new_group = Groups(name=group, creator=random.choice(creators))
        db.add(new_group)
    db.commit()

    groups = db.query(Groups).all()
    assign_none = [random.randint(0, len(data["users"]) - 1) for _ in range(30)]

    for i, user in enumerate(data["users"]):
        if i in assign_none:
            group = None  # None == don't join any groups
        else:
            group = random.choice(groups)
        new_user = Users(name=user, group=group, creator=random.choice(creators))
        db.add(new_user)
    db.commit()
    
    starter = len(data["groups"])
    for i, de_group in enumerate(data["deactivated_groups"]):
        new_group = Groups(name=de_group, creator=random.choice(creators))
        db.add(new_group)
        # deactivate a group
        group = db_session.query(Groups).filter(Groups.id == starter+i+1).one_or_none()
        group.is_activate = False
        group.modifier = random.choice(["Alice", "Bob", "Charlie", "David", "Eve"])  # Mock modifiers
        db.commit()

    print("Successfully populated data!")
    db.close()


if __name__ == "__main__":
    with open("data/example_data.json", "r") as f:
        data = json.load(f)

    db_session = SessionLocal()
    populate_data(db_session, data)
    db_session.close()
