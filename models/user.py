from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional
from datetime import datetime


# Base schema for shared fields
class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True  # Defaults to active


# Schema for user creation (input model)
class UserCreate(UserBase):
    pass  # Inherits fields from UserBase; no additional fields


# Schema for user update (input model)
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None  # Optional fields for partial updates
    updated: Optional[datetime] = None


# Schema for user response (output model)
class UserResponse(UserBase):
    id: UUID
    updated: Optional[datetime]

