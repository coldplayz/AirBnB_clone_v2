#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # Class attributes for database storage
    id = Column(String(60), primary_key=True)
    created_at = Column(Date, nullable=False, default=datetime.utcnow)
    updated_at = Column(Date, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            try:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
            except KeyError:
                pass

            try:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
            except KeyError:
                pass

            try:
                del kwargs['__class__']
            except KeyError:
                pass
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # Remove _sa_instance_state
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        ''' BaseModel interface to storage.delete(),
        for deleting current instance.
        '''
        storage.delete(self)
