#!/usr/bin/python3
"""
File that defines the City class, which inherits from the Base class
and represents the "cities" table in the database.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class represents the "cities" table in the database.
    It inherits from the Base class, which provides the mapping
    between the Python object and the database table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
