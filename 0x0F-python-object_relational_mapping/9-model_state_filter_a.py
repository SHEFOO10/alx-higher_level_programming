#!/usr/bin/python3
""" query states table with specific conditions """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def filter_states():
    """ list all objects that contain the 'a' """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    filter_states()
