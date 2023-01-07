#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import (
        Table, Column, ForeignKey, Integer, String, Numeric, Date, Float)
from models.review import Review
from models.amenity import Amenity

# Create Table object as association table
place_amenity = Table('place_amenity', Base.metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id', ondelete='CASCADE', onupdate='CASCADE'),
                          primary_key=True
                          ),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id', ondelete='CASCADE', onupdate='CASCADE'),
                          primary_key=True
                          )
                      )


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
    amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            backref='place_amenities',
            viewonly=False,
            cascade='all, delete-orphan'
            )

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

    @property
    def amenities(self):
        ''' Getter attribute that returns the list of Amenity
        instances where id is in amenity_ids list.
        '''
        from models import storage

        # Fetch all Amenity objects in storage
        amenities = storage.all(cls=Amenity)  # returns a dictionary of objects

        # Get those amenities related to this instance
        my_amenities = []
        '''
        for obj in amenities.values():
            # Populate amenity_ids incase getter is called first before setter
            self.amenities = obj
        '''

        for obj in amenities.values():
            # List of amenity ids now populated
            if obj.id in Place.amenity_ids:
                # ID match
                my_amenities.append(obj)

        return my_amenities

    @amenities.setter
    def amenities(self, obj=None):
        ''' Setter that handles appending amenity ids to amenity_ids list.

            Args:
                obj (Amenity): an Amenity object. Defaults to None.
        '''
        if type(obj) is Amenity:
            Place.amenity_ids.append(obj.id)
