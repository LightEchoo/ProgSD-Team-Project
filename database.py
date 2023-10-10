from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String)

sql_project = create_engine('sqlite:////sql_project.db', echo=True)
Base = declarative_base()

class User(Base):
    __tanlename__ = 'users'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String(32))
    UserPassword = Column(String(32))
    UserType = Column(Integer)
    UserDebt = Column(Integer, notnull)

