#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE', default='file') == 'db',
            'database storage in use')
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
