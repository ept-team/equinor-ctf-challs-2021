from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask_login  import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String,unique=True)
    password = Column(String)
    

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(String)
    title = Column(String)
    user_id = Column("user_id", Integer)

engine = create_engine(f"sqlite:///pwn.sqlite3")
Base.metadata.create_all(bind=engine)