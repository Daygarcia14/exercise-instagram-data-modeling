import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    post = relationship("post")
    name = Column(String(50), nullable=False, unique = True)
    password = Column(String(8), nullable=False, unique = True)
    email = Column(String(50), nullable=False, unique = True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    imagen = Column(String(50), nullable = False, unique = True)
    caption = Column(String(50), nullable = False, unique = True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Saved(Base):
    __tablename__ = 'saved'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Liked(Base):
    __tablename__ = 'liked'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e