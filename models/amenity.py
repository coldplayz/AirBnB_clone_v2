#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date


class Amenity(BaseModel, Base):
    ''' Definition of Amenity class. '''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Relationships
