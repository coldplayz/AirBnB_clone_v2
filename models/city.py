#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(
            String(60),
            ForeignKey('states.id', ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False)
    name = Column(String(128), nullable=False)

    # Relationships
    places = relationship(
            'Place', backref='cities', cascade="all, delete-orphan")
