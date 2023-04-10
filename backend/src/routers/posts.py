from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from passlib.context import CryptContext
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from .auth import get_current_user
import json


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/post",
    tags=["post"],
    responses={401: {"user": "Not authenticated"}}
)

class postModel(BaseModel):
    timestamp: str
    reference: str
    text: str
    pet_id: int

class postToDelete(BaseModel):
    id: int

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@router.get('/')
async def get_all_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"posts": posts}

@router.get('/comments')
async def get_all_comments(db:Session = Depends(get_db)):
    comments = db.query(models.Comments).all()
    return {"comments": comments}

@router.get('/likes')
async def get_all_likes(db:Session = Depends(get_db)):
    likes = db.query(models.Likes).all()
    return {"likes": likes}

@router.get('/pets')
async def get_all_pets(db:Session = Depends(get_db)):
    pets = db.query(models.Pets).all()
    return {"pets": pets}

@router.get('/follows')
async def get_all_follows(db:Session = Depends(get_db)):
    follows = db.query(models.Follows).all()
    return {"follows": follows}

@router.post('/')
async def new_post(request:Request,post:postModel,db:Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return {"msg": "Authentication error"}
    post_model = models.Posts()
    post_model.timestamp = post.timestamp
    post_model.reference = post.reference
    post_model.pet_id = int(post.pet_id)
    post_model.text = post.text
    post_model.owner_id = user.get("id")
    db.add(post_model)
    db.commit()
    return {"msg": "succesfully created","post":post,"user":user}
    
@router.post('/post/delete')
async def delete_post(post: postToDelete,request:Request,db:Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return False
    post = db.query(models.Posts).filter(models.Posts.id == post.id)\
        .filter(models.Posts.owner_id == user.id).first()
    if post is None:
        return False
    db.delete(post)
    db.commit()
    return True

