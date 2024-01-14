#!/usr/bin/python3
""" delete State object from the database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


def delete_state():
    """ delete state record """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_state()
