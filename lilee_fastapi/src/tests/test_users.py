from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)


"""
add_user has 3 senarios:
1. valid group > exist & activated
2. deactivated grouop > exist but deactivated
3. inexisted group？
"""


@patch("src.common.database.SessionLocal")
@patch("src.repositories.groups.GroupRepository.get_single_group")
def test_add_user_with_valid_group(stub_get_single_group, _):
    # Arrange
    mock_group = MagicMock()
    mock_group.is_activate = True
    stub_get_single_group.return_value = mock_group
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 1})
    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"


@patch("src.common.database.SessionLocal")
@patch("src.repositories.groups.GroupRepository.get_single_group")
def test_add_user_with_deavtivated_group(stub_get_single_group, _):
    # Arrange
    mock_group = MagicMock()
    mock_group.is_activate = False
    stub_get_single_group.return_value = mock_group
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 22})
    # Assert
    assert response.status_code == 400


@patch("src.common.database.SessionLocal")
@patch("src.repositories.groups.GroupRepository.get_single_group")
def test_add_user_with_inexisted_group(stub_get_single_group, _):
    # Arrange
    stub_get_single_group.return_value = None
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 100})
    # Assert
    assert response.status_code == 404
