from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="The title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Detailed description of the todo item")
    completed: bool = Field(False, description="Completion status of the todo item")

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="The title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Detailed description of the todo item")
    completed: Optional[bool] = Field(None, description="Completion status of the todo item")

class Todo(TodoBase):
    id: int = Field(..., description="Unique identifier for the todo item")
    created_at: datetime = Field(..., description="Timestamp when the todo item was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when the todo item was last updated")

    class Config:
        from_attributes = True
