from pydantic import BaseModel


class AuthDetails(BaseModel):
    email: str
    password: str


class Access(BaseModel):
    type: str
    uid: str


class NewUser(BaseModel):
    name: str
    email: str
    username: str
    flag: str
    phone: str
    breed: str
    color: str
    type: str
    image: str
    password: str


class User(BaseModel):
    name: str
    email: str
    username: str
    flag: str
    id: str
    phone: str
    breed: str
    color: str
    type: str
    image: str

