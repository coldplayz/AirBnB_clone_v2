#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    # Implement database storage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    # Implement file storage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

'''
__all__ = [
'base_model', 'user', 'city', 'state', 'place', 'amenity', 'review']
'''
