#!/usr/bin/python3
"""List objects that contain the letter a """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker


def main(argv):

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main(argv)
# Jelly-jonespixel