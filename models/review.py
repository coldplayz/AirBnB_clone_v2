#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from os import getenv


if getenv('HBNB_TYPE_STORAGE', default='file') == 'db':
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = 'reviews'

        place_id = Column(
                String(60),
                ForeignKey(
                    'places.id', ondelete='CASCADE', onupdate='CASCADE'),
                nullable=False
                )
        user_id = Column(
                String(60),
                ForeignKey(
                    'users.id', ondelete='CASCADE', onupdate='CASCADE'),
                nullable=False
                )
        text = Column(String(1024), nullable=False)
else:
    class Review(BaseModel):
        ''' Review for file storage '''
        place_id = ''
        user_id = ''
        text = ''
