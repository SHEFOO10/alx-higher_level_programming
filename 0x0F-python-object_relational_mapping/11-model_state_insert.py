#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


def insert_state():
    """ Insert new state to states Table """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == '__main__':
    insert_state()
