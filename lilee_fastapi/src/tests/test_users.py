from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app


client = TestClient(app)


"""
add_user has 3 senarios:
1. valid group > exist & activated
2. deactivated grouop > exist but deactivated
3. inexisted group
"""


@patch("common.database.SessionLocal")
@patch("services.groups.GroupService.is_group_activated")
def test_add_user_with_valid_group(stub_is_group_activated, stub_session):
    # Arrange
    stub_is_group_activated.return_value = True
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 1})
    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"


@patch("common.database.SessionLocal")
@patch("services.groups.GroupService.is_group_activated")
def test_add_user_with_deavtivated_group(stub_is_group_activated, stub_session):
    # Arrange
    stub_is_group_activated.return_value = False
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 22})
    # Assert
    assert response.status_code == 400


@patch("common.database.SessionLocal")
@patch("repositories.groups.GroupRepository.get_single_group")
def test_add_user_with_inexisted_group(stub_get_single_group, stub_session):
    # Arrange
    stub_get_single_group.return_value = False
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 100})
    # Assert
    assert response.status_code == 404
