from pydantic import BaseModel



class Post(BaseModel):
    title: str
    comment: str
    published: bool = True


class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True


class UpdatePost(BaseModel):
    title: str
    content: str
    published: bool   # There wont be a default for published (bool = True)  because we want to explicit provide each column.


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    title: str
    content: str
    published: bool = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime

    class Config:
        orm_mode = True












