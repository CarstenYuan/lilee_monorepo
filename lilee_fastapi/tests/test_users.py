from fastapi.testclient import TestClient
from unittest.mock import patch
from app.app import app

from app.repositories.database import SessionLocal


client = TestClient(app)


"""
add_user has 4 senarios:
1. valid group > exist & activated
2. without group
3. deactivated grouop > exist but deactivated
4. inexisted group
"""
@patch('app.repositories.database.SessionLocal')
def test_add_user_with_valid_group(mock_session):
    # Act
    response = client.post("/addUser", json={"id": 1, "name": "Alice", "group_id": 1})
    # Assert
    assert response.status_code == 200


@patch('app.repositories.database.SessionLocal')
def test_add_user_without_group(mock_session):
    # Act
    response = client.post("/addUser", json={"id": 1, "name": "Alice", "group_id": None})
    # Assert
    assert response.status_code == 200


@patch('app.repositories.database.SessionLocal')
@patch('app.services.user_service.UserService.is_group_activated')
def test_add_user_with_deavtivated_group(mock_is_group_activated, mock_session):
    # Arrange
    mock_is_group_activated.return_value = False
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 22})
    # Assert
    assert response.status_code == 400


@patch('app.repositories.database.SessionLocal')
@patch('app.repositories.user_repository.UserRepository.get_single_group')
def test_add_user_with_inexisted_group(mock_get_single_group, mock_session):
    # Arrange
    mock_get_single_group.return_value = False
    # Act
    response = client.post("/addUser", json={"name": "Alice", "group_id": 100})
    # Assert
    assert response.status_code == 404
