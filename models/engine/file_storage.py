#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls_objects = {}

        if cls:
            for key in FileStorage.__objects.keys():
                if type(FileStorage.__objects[key]) is cls:
                    # Object is of required type
                    cls_objects.update({key: FileStorage.__objects[key]})
            return cls_objects

        # cls is None; return all __objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' Deletes an object from __objects dictionary.
            Note: if obj is None,
            or non-existent in __objects, nothing should be done
        '''
        # Make a copy of __objects to avoid changing size while iterating
        obj_cpy = FileStorage.__objects.copy()

        if obj:
            for key in obj_cpy.keys():
                if obj is obj_cpy[key]:
                    del FileStorage.__objects[key]

    def close(self):
        ''' Reloads objects.
        '''
        self.reload()
