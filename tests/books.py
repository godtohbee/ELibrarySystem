import pytest
from fastapi.testclient import TestClient
from main import app
from crud.books import books


client = TestClient(app)

@pytest.fixture
def book():
    response = client.post("/books", json=books)
    return response.json()

# test cases for the book endpoints
def test_create_book():
    new_book = {
        "name": "Test Book",
        "author": "Test Author",
        "title": "Test Title"
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Test Successful"
    assert data["data"]["name"] == new_book["name"]
    assert data["data"]["author"] == new_book["author"]
    assert data["data"]["title"] == new_book["title"]
    assert "id" in data["data"]
    
    
def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    

def test_get_book(book):
    book_id = book["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id
    
    
def test_update_book(book):
    book_id = book["id"]
    book_data = {
        "name": "Updated Test Book Name",
        "author": "Updated Test Author",
        "title": "Updated Test Title",
        "description": "An Updated Good Book"
    }
    response = client.put(f"/books/{book_id}", json=book_data)
    assert response.status_code == 200
    data = response.json()
    assert response.json()["name"] == "Updated Test Book Name"
    assert response.json()["title"] == "Updated Title"
    assert response.json()["author"] == "Updated Test Author"
    assert response.json()["description"] == "An Updated Good Book "
    assert "id" in data["data"]
    
    
def test_delete_book(book):
    book_id = book["id"]
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"
    response = client.get("book/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"
    
    
# test cases for book availablibility
def test_get_available_books():
    response = client.get("/books/available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    
def test_mark_unavailable(book):
    book_id = book["id"]
    response = client.patch(f"/books/{book_id}/unavailable")
    assert response.status_code == 200
    assert response.json()["available"] is False