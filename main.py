from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models,schemas,crud_user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/articles")
def read_articles(status: bool, limit: Optional[int] = None):
    return {"message": f"{limit},{status} of data"}


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create(db=db, user=user)

@app.get("/users" , response_model = schemas.UserBase)
def get_users(db: Session = Depends(get_db)):
    users = crud_user.all(db = db)
    
    # return crud_user.get_users(db = db)
