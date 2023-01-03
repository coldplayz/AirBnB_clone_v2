#!/usr/bin/python3
""" Module for testing the console"""
import unittest
import console
import os
import sys
from io import StringIO
from unittest.mock import patch

interpreter = console.HBNBCommand()


class test_console(unittest.TestCase):
    """ Class to test the console """

    def setUp(self):
        """ Set up test environment """
        # Clear storage
        storage = console.storage
        storage._FileStorage__objects.clear()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
            pass
        except:
            pass

    def test_createUser(self):
        ''' Tests the console's `create User` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create User email="obisann@gmail.com" password="myPassword" first_name="Greenbel" last_name="Eleghasim"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            user = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(user.email), str)
            self.assertIs(type(user.password), str)
            self.assertIs(type(user.first_name), str)
            self.assertIs(type(user.last_name), str)

    def test_createState(self):
        ''' Tests the console's `create State` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create State name="Lagos"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            state = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(state.name), str)

    def test_createCity(self):
        ''' Tests the console's `create City` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create City state_id="123ef-5a" name="Ikeja"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            city = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(city.name), str)
            self.assertIs(type(city.state_id), str)

    def test_createAmenity(self):
        ''' Tests the console's `create Amenity` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create Amenity name="street_lights"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            amenity = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(amenity.name), str)

    def test_createPlace(self):
        ''' Tests the console's `create Place` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create Place city_id="2904e-1d9" user_id="ab0f17-ff5" name="bar_beach" description="A_place_to_enjoy_the_cool_Atlantic_ocean_breeze" number_rooms=10 number_bathrooms=20 max_guest=10 price_by_night=50 latitude=37.773972 longitude=-122.431297')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            place = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(place.city_id), str)
            self.assertIs(type(place.user_id), str)
            self.assertIs(type(place.name), str)
            self.assertIs(type(place.description), str)
            self.assertIs(type(place.number_rooms), int)
            self.assertIs(type(place.number_bathrooms), int)
            self.assertIs(type(place.max_guest), int)
            self.assertIs(type(place.price_by_night), int)
            self.assertIs(type(place.latitude), float)
            self.assertIs(type(place.longitude), float)

    def test_createReview(self):
        ''' Tests the console's `create Review` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create Review place_id="73e24-990" user_id="386aa-123" text="This_is_a_place_to_be"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            review = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(review.place_id), str)
            self.assertIs(type(review.user_id), str)
            self.assertIs(type(review.text), str)
