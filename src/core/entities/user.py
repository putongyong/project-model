from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    full_name: Optional[str] = None
