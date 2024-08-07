# app/application/schemas/user_schemas.py
from uuid import UUID

from pydantic import BaseModel, EmailStr
from fastapi import Form


class UserCreateInputDto(BaseModel):
    username: str
    email: EmailStr
    phone: str
    password: str


class UserLoginInputDto(BaseModel):
    email: EmailStr
    password: str


class UserOutputDto(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
    phone: str


class UserLoginDTO(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...),
    ) -> "UserLoginDTO":
        return cls(username=username, password=password)


class UserCreateDTO(BaseModel):
    username: str
    email: str
    phone: str
    password: str


class User(BaseModel):
    username: str
    email: str
    phone: str
