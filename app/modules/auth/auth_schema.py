from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SignupDto(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(max_length=11, min_length=11, default=None)
    password: str = Field(min_length=8)

class SigninDto(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(max_length=11, min_length=11, default=None)
    password: str = Field(min_length=8)

