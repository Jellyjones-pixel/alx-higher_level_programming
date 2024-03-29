#!/usr/bin/python3
"""Start link class to table in database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(argv):

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}' .format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    main(argv)
# Jelly-jonespixel