import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_create_user(client: TestClient, sample_user_data):
    """Test creating a new user."""
    response = client.post("/api/v1/users/", json=sample_user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == sample_user_data["email"]
    assert data["first_name"] == sample_user_data["first_name"]
    assert data["last_name"] == sample_user_data["last_name"]
    assert "id" in data
    assert "created_at" in data

def test_get_users(client: TestClient, sample_user_data):
    """Test getting list of users."""
    # Create a user first
    client.post("/api/v1/users/", json=sample_user_data)
    
    # Get users
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_get_user_by_id(client: TestClient, sample_user_data):
    """Test getting a specific user by ID."""
    # Create a user first
    create_response = client.post("/api/v1/users/", json=sample_user_data)
    created_user = create_response.json()
    user_id = created_user["id"]
    
    # Get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == sample_user_data["email"]

def test_get_nonexistent_user(client: TestClient):
    """Test getting a user that doesn't exist."""
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user_invalid_email(client: TestClient):
    """Test creating a user with invalid email."""
    invalid_data = {
        "email": "invalid-email",
        "first_name": "Test",
        "last_name": "User"
    }
    response = client.post("/api/v1/users/", json=invalid_data)
    assert response.status_code == 422  # Validation error
