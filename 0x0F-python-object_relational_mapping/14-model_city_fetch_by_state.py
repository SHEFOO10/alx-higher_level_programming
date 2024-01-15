#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import Session
from sys import argv


def list_cities():
    """ list cities on specific state """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    ))
    session = Session(bind=engine)
    Base.metadata.create_all(engine)

    cities = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in cities:
        print('{}: ({}) {}'.format(
            state.name,
            city.id,
            city.name
        ))
    session.close()


if __name__ == '__main__':
    list_cities()
