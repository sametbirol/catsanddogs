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


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/post",
    tags=["post"],
    responses={401: {"user": "Not authenticated"}}
)
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