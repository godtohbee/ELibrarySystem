from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

# Base schema for shared fields
class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True  # Defaults to available


# Schema for book creation (input model)
class BookCreate(BookBase):
    pass  # Inherits fields from BookBase; no additional fields


# Schema for book update (input model)
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    is_available: bool | None = None  # Optional fields for partial updates
    updated: Optional[datetime]


# Schema for book response (output model)
class BookResponse(BookBase):
    id: UUID
    updated: Optional[datetime]
