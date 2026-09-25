from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Schema de dados de entrada do user
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema de saída dos dados do user
class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserListSchema(BaseModel):
    users: List[UserPublicSchema]


