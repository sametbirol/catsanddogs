from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.responses import HTMLResponse

models.Base.metadata.create_all(bind=engine)

class CreateUser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    verify_password: str

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authenticated"}}
)
# class Loginuser():
#     def __init__(self, request: Request):
#         self.request: Request = request
#         self.username: Optional[str] = None
#         self.password: Optional[str] = None
#         self.email: Optional[str] = None
#         self.firstname: Optional[str] = None
#         self.lastname: Optional[str] = None

#     async def create_oath_user(self):
#         user = await self.request.user()
#         self.username = user.get("username")
#         self.password = user.get("password")
#         self.email = user.get("email")
#         self.firstname = user.get("firstname")
#         self.lastname = user.get("lastname")

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
async def create_new_user(user: CreateUser,db:Session = Depends(get_db)):
    try:
        validation1= db.query(models.Users).filter(models.Users.username == user.username).first()
        validation2= db.query(models.Users).filter(models.Users.email == user.email).first()

        if user.password != user.verify_password:
            msg = "Passwords do not match"
            return {"msg":msg}
        if validation1 is not None or validation2 is not None:
            msg = "Invalid register request"
            return {"msg":msg}
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
        return {"msg":msg}
    except HTTPException:
        msg = "Unknown Error Occured"
        return {"msg": msg}