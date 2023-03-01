
# to move up directories, in this case twice, therefore, 2 dots

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import Session
from .. import models, schemas, utils
# Move up two directores as you can see routers and app directories , timecode in video 6:22:00
from ..database import get_db, 



router = APIRouter()
@router.post("/users", status_code=Status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Hash the password - user.password()
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get information about a specific user
@router.get('/users/{id}')
# get id and validate it as an integer
def get_user(id: int, db: Session = Depends(get_db)):
    # Store this in a variable called user
    user = db.query(models.User).filter(models.user.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    # If user is found, then user [name] will be returned
    return user