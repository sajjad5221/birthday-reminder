from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.api import users

router = APIRouter()


@router.post("/users", tags=['users'])
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return users.create(db=db, user=user)


@router.get("/users", response_model=schemas.UserBase, tags=['users'])
def get_users(db: Session = Depends(database.get_db)):
    return users.all(db=db)