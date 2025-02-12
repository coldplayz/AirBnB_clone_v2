#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models import storage
import os

if os.getenv('HBNB_TYPE_STORAGE', default='db') == 'file':
    storage.__class__._FileStorage__file_path = 'test.json'

    class test_fileStorage(unittest.TestCase):
        """ Class to test the file storage method """
        def setUp(self):
            """ Set up test environment """
            del_list = []
            for key in storage._FileStorage__objects.keys():
                del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]

        def tearDown(self):
            """ Remove storage file at end of tests """
            try:
                os.remove('test.json')
            except Exception:
                pass

        def test_obj_list_empty(self):
            """ __objects is initially empty """
            self.assertEqual(len(storage.all()), 0)

        def test_new(self):
            """ New object is correctly added to __objects """
            new = BaseModel()
            for obj in storage.all().values():
                temp = obj
            self.assertTrue(temp is obj)

        def test_all(self):
            """ __objects is properly returned """
            new = BaseModel()
            temp = storage.all()
            self.assertIsInstance(temp, dict)

        def test_allFilter(self):
            ''' Tests all() with class filter. '''
            newUser = User()
            newUser.save()
            newState = State()
            newState.save()

            # Retrieve a User object and test
            users = storage.all(User)  # expecting one object - a User

            # TEST that number of retrieved objects is one, not 2
            self.assertEqual(len(users), 1)

            # TEST that retrieved object is a User
            for obj in users.values():
                self.assertIs(type(obj), User)

        def test_delete(self):
            ''' Tests delete() method. '''
            newUser = User()  # newUser is automatically added to __objects

            lenBeforeDel = len(storage.all())

            # Delete the new, and only, object in __objects
            storage.delete(newUser)

            lenAfterDel = len(storage.all())

            # TEST that lone object was actually deleted
            self.assertEqual(lenBeforeDel - lenAfterDel, 1)

        def test_base_model_instantiation(self):
            """ File is not created on BaseModel save """
            self.assertFalse(os.path.exists('test.json'))
            new = BaseModel()
            self.assertTrue(os.path.exists('test.json'))

        def test_empty(self):
            """ Data is saved to file """
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(os.path.getsize('test.json'), 0)

        def test_save(self):
            """ FileStorage save method """
            new = BaseModel()
            storage.save()
            self.assertTrue(os.path.exists('test.json'))

        def test_reload(self):
            """ Storage file is successfully loaded to __objects """
            new = BaseModel()
            storage.save()
            storage.reload()
            for obj in storage.all().values():
                loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

        def test_reload_empty(self):
            """ Load from an empty file """
            with open('test.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()

        def test_reload_from_nonexistent(self):
            """ Nothing happens if file does not exist """
            self.assertEqual(storage.reload(), None)

        def test_base_model_save(self):
            """ BaseModel save method calls storage save """
            new = BaseModel()
            new.save()
            self.assertTrue(os.path.exists('test.json'))

        def test_type_path(self):
            """ Confirm __file_path is string """
            self.assertEqual(type(storage._FileStorage__file_path), str)

        def test_type_objects(self):
            """ Confirm __objects is a dict """
            self.assertEqual(type(storage.all()), dict)

        def test_key_format(self):
            """ Key is properly formatted """
            new = BaseModel()
            _id = new.to_dict()['id']
            for key in storage.all().keys():
                temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

        def test_storage_var_created(self):
            """ FileStorage object storage created """
            from models.engine.file_storage import FileStorage
            print(type(storage))
            self.assertEqual(type(storage), FileStorage)
