#!/usr/bin/python3
"""create a class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
meta_data = MetaData()
Base = declarative_base(MetaData=meta_data)
class State(Base):
    __tablename__ = states
    id = Column(Integer, primary_key=True, unique=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
