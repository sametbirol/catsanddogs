from fastapi import Depends, Form, HTTPException, Request, Response, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm

# bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authenticated"}}
)



class user(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    verify_password: str
    
    
# def get_password_hash(password):
#     return bcrypt_context.hash(password)
# 
# def verify_password(plain_password, hash_password):
#     return bcrypt_context.verify(plain_password, hash_password)
    
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def auth_main(db:Session = Depends(get_db)):
    return ["hello","heloooo"]

@router.post("/")
async def create_new_user(user:user,db:Session = Depends(get_db)):

    try:
        validation1= db.query(models.Users).filter(models.Users.username == user.username).first()
        validation2= db.query(models.Users).filter(models.Users.email == user.email).first()
        
        if validation1 is not None or validation2 is not None:
            msg = "Invalid register request"
            return {"request":user,"msg":msg}
        if user.password != user.verify_password:
            return "Passwords does not match"
        user_model= models.Users()
        user_model.email = user.email
        user_model.first_name = user.first_name
        user_model.last_name =user.last_name
        user_model.hashed_password = user.password
        user_model.username = user.username
        user_model.is_active: bool = True
        db.add(user_model)
        db.commit()
        msg = "User succesfully created"
        return {"request":user,"msg":msg}
    except HTTPException:
        msg = "Unknown Error Occured"
        return {"request": user, "msg": msg}
    
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
#                                  db: Session = Depends(get_db)):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(status_code=404, detail="user not found")
#     return "User Validated"