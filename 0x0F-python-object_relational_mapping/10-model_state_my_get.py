#!/usr/bin/python3
"""
script that prints the state obj with the name
passed as arg from the db
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_user, db_password, db_name, state_name = sys.argv[1:5]

    db_engine = create_engine(f'mysql+mysqldb://{db_user}:{db_password}@'
                              f'localhost:3306/{db_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    states = db_session.query(State).filter(State.name.like(state_name))

    if states.count() != 1 or not states:
        print("Not found")
    else:
        print("{}".format(states.first().id))

    db_session.close()
