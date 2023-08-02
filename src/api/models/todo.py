from datetime import datetime
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None
    completed: bool = False