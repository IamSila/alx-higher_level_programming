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
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.commit()
    session.close()
