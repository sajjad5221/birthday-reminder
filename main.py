from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/articles")
def read_articles(status: bool, limit: Optional[int] = None):
    return {"message": f"{limit},{status} of data"}


# @app.post("/user")
# def register(request: models.User):
#     return {"email": request.email}
