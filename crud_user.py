from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
import models,schemas, hashing

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create(db: Session, user: schemas.UserCreate):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=422, detail="User exist")
    else:
        db_user = models.User(
            email=user.email, hashed_password=hashing.Hash.bcrypt(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def find_by_email(db: Session, email):
    return db.query(models.User).filter(models.User.email == email).first()
    

def authenticate_user(db: Session, email, password):
    user = find_by_email(email)
    if not user:
        return False
    if not verify_password(password, get_password_hash(user.password)):
        return False
    return True
    