#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from os import getenv


if getenv('HBNB_TYPE_STORAGE', default='file') == 'db':
    class Amenity(BaseModel, Base):
        ''' Definition of Amenity class. '''
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        # Relationships
else:
    class Amenity(BaseModel):
        ''' Amenity for file storage '''
        name = ''
