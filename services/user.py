from fastapi import HTTPException
from models.user import UserCreate, UserResponse
from crud.user import UserCRUD

class UserService:
    @staticmethod
    def create_user(user_data: UserCreate) -> UserResponse:
        create_user = UserCRUD.create_user(user_data)
        return UserResponse(**create_user.model_dump())

    @staticmethod
    def get_user_by_id(user_id: str) -> UserResponse:
        user = UserCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return UserResponse(**user.model_dump())

    @staticmethod
    def get_all_users() -> list[UserResponse]:
        users = UserCRUD.get_all_users()
        return [UserResponse(**user.model_dump()) for user in users]

    @staticmethod
    def update_user(user_id: str, user_data: UserCreate) -> UserResponse:
        #updates user details
        updated_user = UserCRUD.update_user(user_id, user_data)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found.")
        return UserResponse(**updated_user.model_dump())

    @staticmethod
    def deactivate_user(user_id: str) -> UserResponse:
        # deactivates a user account and raises HTTPException if user not found and check if user exists
        user = UserCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )
        # if user is already deactivated, return error
        if not user.is_active:
            raise HTTPException(
                status_code=400,
                detail="User is already deactivated."
            )
        # deactivate the user
        updated_user = UserCRUD.deactivate_user(user_id)
        return UserResponse(**updated_user.model_dump())

    @staticmethod
    def reactivate_user(user_id: str) -> UserResponse:
        # reactivates a deactivated user account and raises HTTPException if user not found or already active.
        user = UserCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )
        if user.is_active:
            raise HTTPException(
                status_code=400,
                detail="User is already active."
            )
        updated_user = UserCRUD.reactivate_user(user_id)
        return UserResponse(**updated_user.model_dump())    