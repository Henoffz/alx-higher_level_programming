#!/usr/bin/python3
"""
script to list all obj that contain letter a
takes 3 args
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        exit()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    state = session().query(State).filter(State.name.like('%a%')).order_by(
        State.id).all()

    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")

    session.close()
