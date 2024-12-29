from fastapi import APIRouter
from typing import Optional
from schemas.users import UserCreate, UserUpdate, User
from uuid import UUID
from crud.users import users_crud


user_router = APIRouter()


@user_router.get("/", summary="Get all users", status_code=200)
def get_all_users():    
    return {
        "message": "Users retrieved successfully",
        "data": users_crud.get_all_users()
    }
    
    
@user_router.get("/{user_id}", summary="Get a user", status_code=200)
def get_user(user_id: UUID):
    return{
        "mesaage": "User retrieved successfully",
        "data": users_crud.get_user(user_id)
    }


@user_router.post("/", summary="Create a new user", status_code=201)
def create_user(payload: UserCreate):
    new_user = users_crud.create_user(payload)
    return {
        "message": "User created successfully",
        "data": new_user
    }
    

@user_router.put("/{user_id}", summary="Update user details", status_code=200)
def update_user(user_id: UUID, payload: UserUpdate):
    user: Optional[User] = users_crud.get_user(user_id)
    update_user = users_crud.update_user(user, payload)    
    return {
        "message": "User updated successfully",
        "data": "Updated User"
    }


@user_router.delete("/{user_id}", summary="Delete a user", status_code=200)
def delete_user(user_id: UUID):
    return users_crud.delete_user(user_id)
    
        
@user_router.patch("/{user_id}", summary="Deactivate User", status_code=200)
def deactivate_user(user_id: UUID):
    return {
        "message": f"User {user_id} has been deactivated successfully."
    }
    
    
@user_router.get("/{user_id}", summary="Get users who borrowed books", status_code=200)
def get_user_who_borrowed_books():
    return {
        "message": "Users who borrowed books",
        "data": users_crud.get_user_who_borrowed_books()
    }