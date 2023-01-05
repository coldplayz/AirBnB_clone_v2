#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationships
    places = relationship(
            'Place', backref='user', cascade="all, delete-orphan")
