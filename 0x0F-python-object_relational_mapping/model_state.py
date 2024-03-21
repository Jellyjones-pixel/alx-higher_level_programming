#!/usr/bin/python3
"""Definition of State and instance Base = declarative_base()"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return("<States(id='%s', name='%s')>" % (self.id, self.name))
