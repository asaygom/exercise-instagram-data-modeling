import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

association_table = Table(
    "follower",
    Base.metadata,
    Column("user_from_id", ForeignKey("user.id")),
    Column("user_to_id", ForeignKey("user.id")),
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    comment = relationship("Comment")
    post = relationship("Post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship("Comment")
    media = relationship("Media")

class MediaEnum(enum.Enum):
    jpg = "jpg"
    mp4 = "mp4"

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaEnum), nullable=False)
    url = Column(String, nullable=False)
    post_id= Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
