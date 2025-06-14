import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_create_item(client: TestClient, sample_item_data):
    """Test creating a new item."""
    response = client.post("/api/v1/items/", json=sample_item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == sample_item_data["title"]
    assert data["description"] == sample_item_data["description"]
    assert data["is_active"] == sample_item_data["is_active"]
    assert "id" in data
    assert "created_at" in data

def test_get_items(client: TestClient, sample_item_data):
    """Test getting list of items."""
    # Create an item first
    client.post("/api/v1/items/", json=sample_item_data)
    
    # Get items
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_get_item_by_id(client: TestClient, sample_item_data):
    """Test getting a specific item by ID."""
    # Create an item first
    create_response = client.post("/api/v1/items/", json=sample_item_data)
    created_item = create_response.json()
    item_id = created_item["id"]
    
    # Get the item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["title"] == sample_item_data["title"]

def test_get_nonexistent_item(client: TestClient):
    """Test getting an item that doesn't exist."""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_create_item_minimal_data(client: TestClient):
    """Test creating an item with minimal required data."""
    minimal_data = {
        "title": "Minimal Item"
    }
    response = client.post("/api/v1/items/", json=minimal_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Minimal Item"
    assert data["description"] is None
    assert data["is_active"] is True  # Default value
