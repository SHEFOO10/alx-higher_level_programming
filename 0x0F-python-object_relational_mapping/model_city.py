#!/usr/bin/python3
""" City Model """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base
from sqlalchemy.orm import relationship

class City(Base):
    """ City Model Class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    State = relationship(State)
