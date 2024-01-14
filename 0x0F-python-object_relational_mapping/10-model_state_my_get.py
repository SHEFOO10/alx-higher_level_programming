#!/usr/bin/python3
""" prints the State object with the name passed as argument """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def get_state():
    """ get state object from the database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print('Not found')
    session.close()

if __name__ == '__main__':
    get_state()
