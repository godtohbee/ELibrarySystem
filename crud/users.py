from fastapi import HTTPException
from schemas.users import User, UserCreate, UserUpdate, UserDelete
from uuid import UUID
from datetime import datetime


users = {}
borrow_records = {}

users = [
    User(id=1, username="user1", email="user1@example.com", name="User 1"),
    User(id=2, username="user2", email="user2@example.com", name="User 2"),
    User(id=3, username="user3", email="user3@example.com", name="User 3"),
    User(id=4, username="user4", email="user4@example.com", name="User 4"),
    User(id=5, username="user5", email="user5@example.com", name="User 5"),
]

borrow_records() = {
    "id": str,
    "user_id": str,
    "book_id": int,
    "borrow_date": datetime.now(),
    "return_date": None
    }


class UserCrud:
    @staticmethod
    def get_all_users():
        # check if there are any users in the database
        if not users:
            return {
                "message": "No users found",
                "users": []
            }
        return users
    
    
    @staticmethod
    def get_user(user_id: UUID):
        # check if the user exists in the database
        user = users.get(user_id)
        if not user:
            raise HTTPException(
                status_code=404, detail=f"User with ID {user_id} not found."
                )
        return user
    
    
    @staticmethod
    def create_user(user: UserCreate):
        # check if the email is already registered
        for existing_user in users.values():
            if existing_user["email"] == user.email:
                raise HTTPException(status_code=400, detail="Email already exists")
            # generate a unique ID for the new user
            user_id = str(UUID())
            # create the new user    
        new_user = {
            "id": user_id,
            "name": user.name,
            "email": user.email,
            "is_active": user.is_active,
        }
            # add the new user to the database
        users[user_id] = new_user
        return {
        "message": "User created successfully",
        "user": new_user
        }    
    
    
    @staticmethod
    def update_user(user_id: UUID, user: UserUpdate):
        # check if the user exists in the database
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
            # get the existing user data
        existing_user = users[user_id]
        # update the fields with new values if provided
        if user.name is not None:
            existing_user["name"] = user.name
        if user.email is not None:
        # check if the email is already in use by another user
            for other_user_id, other_user in users.items():
                if other_user_id != user_id and other_user["email"] == user.email:
                    raise HTTPException(status_code=400, detail="Email already in use by another user")
            existing_user["email"] = user.email
        if user.is_active is not None:
            existing_user["is_active"] = user.is_active
        # save the updated user data back to the database
            users[user_id] = existing_user
        return {
            "message": "User updated successfully",
            "user": existing_user
        }
        
        
    @staticmethod
    def delete_user(user_id: UUID, user: UserDelete):  
        # check if the user exists in the database
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
        # remove the user from the database
        deleted_user = users.pop(user_id)
        return {
        "message": "User deleted successfully",
        "user": deleted_user 
        }
    
    
    @staticmethod
    def deactivate_user(user_id: int):
        # check if the user exists in the database
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User Not Found")
        # set the user's active status to False to deactivate the
        users[user_id]["is_active"] = False
        return {
            "message": f"User {user_id} has been deactivated successfully."
        }
        
        
    @staticmethod
    def get_user_who_borrowed_books(user_id: UUID):
        # find borrows for the given user_id
        user_borrowed_books = [borrow for borrow in borrow_records if borrow[user_id] == user_id]
        if not user_borrowed_books:
            raise HTTPException(status_code=404, detail="No borrowed books found for this user")
        return {
            "user_id": user_id,
            "borrowed_books": user_borrowed_books
        }
        
users_crud = UserCrud()