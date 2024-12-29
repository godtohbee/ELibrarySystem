import pytest
from fastapi.testclient import TestClient
from main import app
from crud.users import users
from schemas.users import UserBase, UserCreate, UserUpdate, UserDelete
from typing import List


client = TestClient(app)

@pytest.fixture
def user():
    response = client.post("/users", json=users)
    return response.json()

# test cases for users endpoint
def test_user():
    response = client.post("/users", json=users)
    assert response.status_code == 201
    assert response.json()["name"] == users["name"]
    
    
def test_create_user():
    new_user = {
        "name": "Test Name",
        "email": "Test Email",
        "username": "Test Username"
    }
    response = client.post("/books", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Test Successful"
    assert data["data"]["name"] == new_user["name"]
    assert data["data"]["email"] == new_user["email"]
    assert data["data"]["username"] == new_user["username"]
    assert "username" in data["data"]
    
    
def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    
def test_get_user(user):
    username = user["username"]
    response = client.get(f"/users/{username}")
    assert response.status_code == 200
    assert response.json(["id"]) == username
    
    
def test_update_user(user):
    username = user["username"]
    updated_user_data = {
        "name": "Updated Test Name",
        "email": "Updated Test Email",
        "description": "Updated User"
    }
    response = client.put(f"/users/{username}", json=updated_user_data)
    assert response.status_code == 200
    data = response.json()
    assert response.json()["name"] == "Updated Test Name"
    assert response.json()["email"] == "Updated Test Email"
    assert response.json()["description"] == "Updated User"
    assert "username" in data["data"]


def test_delete_user(user):
    username = user["username"]
    response = client.delete(f"/users/{username}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
    response = client.get("users/")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"