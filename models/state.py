#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship, sessionmaker
from os import getenv


if getenv('HBNB_TYPE_STORAGE', default='file') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)

        # Relationships
        cities = relationship(
                "City", backref='state', cascade='all, delete-orphan')
else:
    class State(BaseModel):
        ''' State for file storage '''
        name = ''

        @property
        def cities(self):
            ''' Getter attribute that returns the list of City
            instances where state_id equals the current State.id
            '''
            from models import storage

            # Get instance id
            state_id = self.id

            # Fetch all City objects in storage
            cities = storage.all(cls=City)  # returns a dictionary of objects

            # Get those cities related to this instance
            my_cities = []
            for obj in cities.values():
                if state_id == obj.state_id:
                    # ID match
                    my_cities.append(obj)

            return my_cities
