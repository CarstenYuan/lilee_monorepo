import json
import random

from ..repositories.models.groups_model import Groups
from ..repositories.models.users_model import Users
from ..common.database import SessionLocal


def populate_data(db, data) -> None:
    creators = ["Admin", "Jay Chou", "Eason Chen", "Carsten Yuan"]

    for group in data["groups"]:
        new_group = Groups(name=group, creator=random.choice(creators))
        db.add(new_group)
    db.commit()

    # deactivated the group Meditation
    group = db.query(Groups).filter(Groups.id == 20).one_or_none()
    group.is_activate = False
    group.modifier = random.choice(
        ["Alice", "Bob", "Charlie", "David", "Eve"]
    )  # Mock modifiers
    db.commit()

    # add users and assign a group or none to them
    groups = db.query(Groups).filter(Groups.is_activate == 1).all()
    assign_none = [random.randint(0, len(data["users"]) - 1) for _ in range(20)]

    for i, user in enumerate(data["users"]):
        group = None if i in assign_none else random.choice(groups)
        new_user = Users(name=user, group=group, creator=random.choice(creators))
        db.add(new_user)
    db.commit()

    print("Successfully populated data!")
    db.close()


if __name__ == "__main__":
    with open("populate_mock_data/mock_data.json", "r", encoding="utf-8") as f:
        fake_data = json.load(f)

    db_session = SessionLocal()
    populate_data(db_session, fake_data)
    db_session.close()
