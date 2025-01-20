from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models.user import UserCreate, UserResponse, UserUpdate
from crud.user import UserCRUD

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    new_user = UserCRUD.create_user(user)
    if not new_user:
        raise HTTPException(status_code=400, detail="User creation failed.")
    return new_user


@user_router.get("/", response_model=List[UserResponse], status_code=200)
def get_all_users():
    return UserCRUD.get_all_users()


@user_router.get("/{user_id}", response_model=UserResponse, status_code=200)
def get_user(user_id: UUID):
    user = UserCRUD.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@user_router.put("/{user_id}", response_model=UserResponse, status_code=200)
def update_user(user_id: UUID, user_data: UserUpdate):
    updated_user = UserCRUD.update_user(user_id, **user_data.model_dump())
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or update failed.")
    return updated_user


@user_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID):
    success = UserCRUD.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User deleted successfully."}


@user_router.patch("/{user_id}/deactivate", response_model=UserResponse, status_code=200)
def deactivate_user(user_id: UUID):
    deactivated_user = UserCRUD.deactivate_user(user_id)
    if not deactivated_user:
        raise HTTPException(status_code=404, detail="User not found or already deactivated.")
    return deactivated_user


@user_router.patch("/{user_id}/reactivate", response_model=UserResponse, status_code=200)
def reactivate_user(user_id: UUID):
    reactivated_user = UserCRUD.reactivate_user(user_id)
    if not reactivated_user:
        raise HTTPException(status_code=404, detail="User not found or already deactivated.")
    return reactivated_user
