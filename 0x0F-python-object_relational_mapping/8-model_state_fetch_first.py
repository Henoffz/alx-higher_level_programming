#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
                       pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
