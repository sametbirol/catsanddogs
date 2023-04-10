from fastapi import Depends, HTTPException, Request, Response, status, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from passlib.context import CryptContext
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
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
    side: str


class loguser(BaseModel):
    username: str
    password: str


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
    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta]):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(request: Request):
    try:
        token = request.cookies.get("access_token")
        if token is None:
            return None
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            # logout(request)
            return None
        return {"username": username, "id": user_id}
    except ExpiredSignatureError:
        return None
    except JWTError:
        return None


@router.get("/")
async def auth_main(request: Request, db: Session = Depends(get_db)):
    userr = await get_current_user(request)
    if userr is None:
        return {"user": userr}
    user = db.query(models.Users).filter(
        models.Users.id == userr.get("id")).first()
    if user is None:
        return {"user": user}
    return {"user": user}


@router.post("/register")
async def register(user: reguser, db: Session = Depends(get_db)):
    validation1 = db.query(models.Users).filter(
        models.Users.username == user.username).first()
    validation2 = db.query(models.Users).filter(
        models.Users.email == user.email).first()
    if user.password != user.verify_password:
        msg = "Passwords do not match"
        return {"msg": msg}
    if validation1 is not None or validation2 is not None:
        msg = "Invalid register request"
        return {"msg": msg}
    user_model = models.Users()
    user_model.email = user.email
    user_model.first_name = user.first_name
    user_model.last_name = user.last_name
    user_model.hashed_password = get_password_hash(user.password)
    user_model.username = user.username
    user_model.side = user.side
    user_model.is_active: bool = True
    db.add(user_model)
    db.commit()
    msg = "User succesfully created"
    return {"msg": msg,"username":user.username,"password":user.password}

@router.post("/token")
async def login_for_access_token(response: Response, form_data,
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return False
    token_expires = timedelta(minutes=30)
    token = create_access_token(
        user.username, user.id, expires_delta=token_expires)
    response.set_cookie(key="access_token", value=token, httponly=True)
    return {"token": token}


@router.post("/login")
async def login_to_user(user: loguser, response: Response, db: Session = Depends(get_db)):
    try:
        # getuser = db.query(models.Users).filter(
        #     models.Users.username == user.username).first()
        validate_user_cookie = await login_for_access_token(response=response, form_data=user, db=db)
        if user.username is None or user.password is None:
            msg = "Username or password cannot be empty"
            return {"request": user, "msg": msg}
        elif not validate_user_cookie:
            msg = "Incorrect Username or Password"
            return {"msg":msg}
        else:
            msg = "Login Succesful"
            # await auth_main()
            return {"msg":msg}

    except HTTPException:
        msg = "Unknown Error Occured"
        return {"request": user, "msg": msg}


@router.get("/logout")
async def logout(request: Request, response: Response, db:Session = Depends(get_db)):
    msg = "Logout successful"
    try:
        userr = await get_current_user(request)
        user = db.query(models.Users).filter(models.Users.id == userr.get("id")).first()
        user.is_active = False
        db.add(user)
        db.commit()
    finally:
        response.delete_cookie(key="access_token")
        return {"msg": msg}

    # response = templates.TemplateResponse("login.html", {"request": request, "msg": msg})


# Exceptions


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
