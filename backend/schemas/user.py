from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
