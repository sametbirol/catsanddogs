from fastapi import FastAPI,Depends
from database import engine
from routers import auth
import models
from fastapi.middleware.cors import CORSMiddleware  # NEW


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)