#Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional
#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
#FastAPI
from fastapi import FastAPI

app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length= 8,
        max_length= 30
    )

class User(UserBase):    
    first_name: str = Field(
        ...,
        min_length= 3,
        max_length= 20
    )
    last_name: str = Field(
        ...,
        min_length= 3,
        max_length= 20
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...),
    content: str = Field(
        ...,
        min_length= 1,
        max_length= 256
    )
    created_at: datetime = Field(datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API" : "Working!"}