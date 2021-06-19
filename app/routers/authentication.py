from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models, schemas, database
from app.api import users
from app.services import token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services.hashing import Hash

router = APIRouter()


@router.post("/auth/login", tags=['Authentication'])
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = users.find_by_email(db=db, email=request.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credential")
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password")
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
