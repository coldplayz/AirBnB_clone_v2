#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import os


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', default='file') == 'db', 'database storage in use')
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
