import pytest
from fastapi.testclient import TestClient
from main import app
from crud.borrow import borrow_records
from crud.books import books
from crud.users import users


client = TestClient(app)

@pytest.fixture
def borrow():
    response = client.post("/borrow", json=borrow_records)
    return response.json()
    
# test cases for borrow endpoints
    
def test_borrow_book():
    borrow_data = {
        "user_id": users["id"],
        "book_id": books["id"]
    }
    response = client.post("/borrow", json=borrow_data)
    assert response.status_code == 201
    assert response.json()["user_id"] == borrow_data["user_id"]
    assert response.json()["book_id"] == borrow_data["book_id"]
    
    
def test_get_all_borrowed_books():
    response = client.get("/borrow")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    
def test_mark_returned():
    borrow_data = {
        "user_id": users["id"],
        "book_id": books["id"]
    }
    borrow_response = client.post("/borrow", json=borrow_data)
    borrow_id = borrow_response.json()["id"]  
    response = client.patch(f"/borrow/{borrow_id}/return")
    assert response.status_code == 200
    assert response.json()["returned"] is True