#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import (
        Column, ForeignKey, Integer, String, Numeric, Date, Float)
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(
            String(60),
            ForeignKey('cities.id', ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False
            )
    user_id = Column(
            String(60),
            ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False
            )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # Relationships
    reviews = relationship(
            'Review', backref='place', cascade="all, delete-orphan")

    # FileStorage relationship implementation
    @property
    def reviews(self):
        ''' Getter attribute that returns the list of Review
        instances where place_id equals the current Place.id
        '''
        from models import storage

        # Get instance id
        place_id = self.id

        # Fetch all Review objects in storage
        reviews = storage.all(cls=Review)  # returns a dictionary of objects

        # Get those reviews related to this instance
        my_reviews = []
        for obj in reviews.values():
            if place_id == obj.place_id:
                # ID match
                my_reviews.append(obj)

        return my_reviews
