from typing import Literal

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from pydantic import BaseModel, Field
from typing import Literal, List
from sqlalchemy import create_engine



class CreateUser(BaseModel):
    image: str
    id: int
    name: str = Field(max_length=40, min_length=3)
    age: int = Field()
    sex: Literal["male", "female"]
    description: str = Field(max_length=300)
    games: list[str] = []
    who_likes: list[int] = []
    recomends: list[int] = []


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    image = Column(String)
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(Integer)
    sex = Column(String(10))
    description = Column(Text)
    games = Column(String) #Json
    who_likes = Column(String)
    recomends = Column(String)


