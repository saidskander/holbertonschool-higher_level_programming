#!/usr/bin/python3
"""
lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    state_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                 sys.argv[1],
                                 sys.argv[2],
                                 sys.argv[3]),
                                 pool_pre_ping=True)
    Base.metadata.create_all(state_engine)

    session = Session(state_engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
