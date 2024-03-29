#!/usr/bin/python3
"""Class definition of City and an instance Base = declarative_base()"""
from sqlalchemy import ForeignKey, Integer, String, Column
from model_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)

    def __repr__(self):
        return("<City(id='%s', name='%s', state_id='%s')>"
               % (self.id, self.name, self.state_id))
# Jelly-jonespixel