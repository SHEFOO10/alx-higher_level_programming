#!/usr/bin/python3
""" update name of state object """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


def update_state():
    """ update state object name """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'

    session.commit()
    session.close()


if __name__ == '__main__':
    update_state()
