#!/usr/bin/python3
"""Deletes states whose name contains 'a'"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_my_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_engine = create_my_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(my_engine)

    Session = sessionmaker(bind=my_engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
