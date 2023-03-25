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



SECRET_KEY = "ymir<3ecm"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authenticated"}}
)

class reguser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    verify_password: str
    
class loguser(BaseModel):
    username:str
    password:str
    
outh2_bearer =  OAuth2PasswordBearer(tokenUrl="token")   

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hash_password):
    return bcrypt_context.verify(plain_password, hash_password)

def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users)\
        .filter(models.Users.username == username).first()
        
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return True


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta]):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = 15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)    


@router.get("/")
async def auth_main(db:Session = Depends(get_db)):
    return ["hello","heloooo"]

@router.post("/register")
async def create_new_user(user:reguser,db:Session = Depends(get_db)):

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
        user_model.hashed_password = get_password_hash(user.password)
        user_model.username = user.username
        user_model.is_active: bool = True
        db.add(user_model)
        db.commit()
        msg = "User succesfully created"
        return {"msg":msg}
    except HTTPException:
        msg = "Unknown Error Occured"
        return {"request": user, "msg": msg}



@router.post("/login")
async def login_to_user(user:loguser, db:Session = Depends(get_db)):
    try:
        if user.username is None or user.password is None:
            msg = "Username or password cannot be empty"
            return {"request": user, "msg":msg}
        getuser = db.query(models.Users).filter(models.Users.username == user.username).first()
        
        if getuser is None:
            get_user_exception()
            
        if authenticate_user(getuser.username, user.password, db):
            token = create_access_token(getuser.username ,getuser.id, timedelta(minutes=10))
            return token
        
    except HTTPException:
        msg = "Unknown Error Occured"
        return {"request": user, "msg": msg}

#Exceptions
def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},   
    )
    return credentials_exception

def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return token_exception_response
