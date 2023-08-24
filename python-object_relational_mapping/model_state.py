#!/usr/bin/python3
"""create a class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from models import Base, State
Base = declarative_base()
class State(Base):
    __tablename__ = states
    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}@localhost/{}port=3306'.format(user, password) 
    Base.metadata.create_all(engine)
