#!/usr/bin/python3
"""Lists all the states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    # Session
    ses = Session()
    # input state query
    state_res = ses.query(State).order_by(State.id).all()
    for item in state_res:
        print('{}: {}'.format(item.id, item.name))
    ses.close()
