#!/usr/bin/python3
""" City Model """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ City Model Class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship(State)
