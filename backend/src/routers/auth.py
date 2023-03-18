from fastapi import Depends, Form, HTTPException, Request, Response, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.responses import HTMLResponse

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authenticated"}}
)
class LoginForm():
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None
        self.firstname: Optional[str] = None
        self.lastname: Optional[str] = None

    async def create_oath_form(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
        self.email = form.get("email")
        self.firstname = form.get("firstname")
        self.lastname = form.get("lastname")

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
async def create_new_user(request:Request,db:Session = Depends(get_db)):
    return ["hello","heloooo"]
    # try:
    #     form = LoginForm(request)
    #     await form.create_oath_form()
    #     validation1= db.query(models.Users).filter(models.Users.username == form.username).first()
    #     validation2= db.query(models.Users).filter(models.Users.email == form.email).first()

    #     if validation1 is not None or validation2 is not None:
    #         msg = "Invalid register request"
    #         return {"request":request,"msg":msg}
    #     user_model= models.Users()
    #     user_model.email = form.email
    #     user_model.first_name = form.firstname
    #     user_model.last_name =form.lastname
    #     user_model.hashed_password = form.password
    #     user_model.username = form.username
    #     user_model.is_active: bool = True
    #     db.add(user_model)
    #     db.commit()
    #     msg = "User succesfully created"
    #     return {"request":request,"msg":msg}
    # except HTTPException:
    #     msg = "Unknown Error Occured"
    #     return {"request": request, "msg": msg}