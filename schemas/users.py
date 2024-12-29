from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    is_active: bool = Field(default=True)
    created: datetime
    updated: datetime
    borrow_date: datetime
    return_date: datetime | None
    returned: bool = Field(default=False)

    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserDelete(UserBase):
    pass

class User(UserBase):
    id = UUID