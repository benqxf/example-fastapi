
# to move up directories, in this case twice, therefore, 2 dots

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import Session
from typing import List

from .. import models, schemas
# Move up two directores as you can see routers and app directories , timecode in video 6:22:00
from ..database import get_db

router = APIRouter(
    # append it with id
    prefix="/posts" 
)


@router.get("/{id}", response_model==schemas.Post)
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return posts


@router.post("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())


