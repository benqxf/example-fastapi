


from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user




models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# @app.get("/app")
# def root():
#     return {"message": "Hello World"}

# @app.post("/createposts")
# def create_posts(payload: dict = Body):

# User  Registration
















 app.include_router(post.router)
 app.include_router(user.router)

 