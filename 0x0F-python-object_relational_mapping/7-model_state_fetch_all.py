#!/usr/bin/python3
"""
lists all State objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    state_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                                 .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                                 pool_pre_ping=True)
    Session = sessionmaker(bind=state_engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
