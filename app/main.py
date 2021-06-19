from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from app.db import models, schemas
from app.routers import users,authentication

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def root():
    return {"hello": "world"}


# @app.post("/users",tags=['users'])
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud_user.create(db=db, user=user)

# @app.get("/users" , response_model = schemas.UserBase ,tags=['users'])
# def get_users(db: Session = Depends(get_db)):
#     users = crud_user.all(db = db)

    # return crud_user.get_users(db = db)
app.include_router(users.router)
app.include_router(authentication.router)
