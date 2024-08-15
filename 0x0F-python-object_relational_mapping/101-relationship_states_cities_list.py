#!/usr/bin/python3
"""Create state California"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_my_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_engine = create_my_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(my_engine)

    Session = sessionmaker(bind=my_engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.commit()
    session.close()
