#!/usr/bin/python3
"""Adds a brand new State to the system!"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(my_engine)

    Session = sessionmaker(bind=my_engine)
    session = Session()
    states = session.query(State).filter(State.id == 2).all()
    if states:
        states[0].name = "New Mexico"
    session.commit()
    session.close()
