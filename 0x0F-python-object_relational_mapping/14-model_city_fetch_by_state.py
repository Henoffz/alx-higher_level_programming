#!/usr/bin/python3
"""
Script that prints all city objects
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    user = argv[1]
    password = argv[2]
    name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    result = (session.query(State, City)
              .filter(State.id == City.state_id)
              .order_by(City.id)
              .all())

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
