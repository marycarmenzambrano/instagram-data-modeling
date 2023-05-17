import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(250), nullable=False)
    user_to_id = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey("follower.id"))
    relacion_follower = relationship(Follower)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)



    def to_dict(self):
        return {}


  person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
