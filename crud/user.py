from uuid import UUID
from typing import List, Optional
from models.user import UserCreate, UserUpdate, UserResponse
from datetime import datetime


class UserCRUD:
    # In-memory storage for users
    users_db: List[UserResponse] = []

    @staticmethod
    def create_user(user: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id = UUID,
            name = user.name,
            email = user.email,
            is_active = True,
            created = datetime.now(),
            updated = datetime.now(),
        )
        UserCRUD.users_db.append(new_user)
        return new_user

    @staticmethod
    def get_user_by_id(user_id: UUID) -> Optional[UserResponse]:
        return next((user for user in UserCRUD.users_db if user.id == user_id), None)

    @staticmethod
    def get_all_users() -> List[UserResponse]:
        return UserCRUD.users_db

    @staticmethod
    def update_user(user_id: UUID, user_update: UserUpdate) -> Optional[UserResponse]:
        user = UserCRUD.get_user_by_id(user_id)
        if user:
            if user_update.name:
                user.name = user_update.name
            if user_update.email:
                user.email = user_update.email
            if user_update.is_active is not None:
                user.is_active = user_update.is_active
            user.updated = datetime.now()
            return user
        return None

    @staticmethod
    def delete_user(user_id: UUID) -> bool:
        initial_count = len(UserCRUD.users_db)
        UserCRUD.users_db = [user for user in UserCRUD.users_db if user.id != user_id]
        return len(UserCRUD.users_db) < initial_count

    @staticmethod
    def deactivate_user(user_id: UUID) -> Optional[UserResponse]:
        user = UserCRUD.get_user_by_id(user_id)
        if user:
            user.is_active = False
            user.updated = datetime.now()
            return user
        return None
    
    @staticmethod
    def reactivate_user(user_id: UUID) -> Optional[UserResponse]:
        user = UserCRUD.get_user_by_id(user_id)
        if user:
            user.is_active = False
            user.updated = datetime.now()
            return None
        return user