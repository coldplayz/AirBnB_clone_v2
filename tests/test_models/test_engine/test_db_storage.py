#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage
import os
from unittest.mock import patch
from io import StringIO
import MySQLdb as mdb
import console

interpreter = console.HBNBCommand()


class test_DBStorage(unittest.TestCase):
    """ Class to test the database storage """
    def setUp(self):
        """ Set up test environment """
        # Prepare database connection parameters
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        dbase = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST')
        port = '3306'

        # Connect to the database
        conn = mdb.connect(host=host, user=user, passwd=passwd, db=dbase)

        # Get a cursor
        cur = conn.cursor()

        self.cursor = cur
        self.connection = conn

    def tearDown(self):
        """ Free resources """
        self.cursor.close()
        self.connection.close()

    @unittest.skipIf(
            os.getenv(
                'HBNB_TYPE_STORAGE', default='file') != 'db',
            'file storage in use')
    def test_create_StateCity(self):
        ''' Tests the creation of a State and associated City instance.
        '''
        cur = self.cursor

        # Prepare query
        qryState = "SELECT * FROM states"
        qryCity = "SELECT * FROM cities"

        # Execute query
        cur.execute(qryState)

        # Get number of rows returned
        state_rowCntBefore = cur.rowcount

        # Add a record with the console
        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create State name="California"')

        # Query database again
        self.reset_conn()
        cur = self.cursor
        cur.execute(qryState)

        # Get new row count
        state_rowCntAfter = cur.rowcount
        # Get state id
        self.reset_conn()
        cur = self.cursor
        cur.execute('SELECT states.id FROM states')
        state_id = cur.fetchall()[0][0]

        # For City
        self.reset_conn()
        cur = self.cursor
        cur.execute(qryCity)
        city_rowCntBefore = cur.rowcount

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd(
                    f'create City name="Fremont" state_id="{state_id}"')

        # Get City row count afterwards
        self.reset_conn()
        cur = self.cursor
        cur.execute(qryCity)
        city_rowCntAfter = cur.rowcount

        # TEST if the state record was persisted to the database
        self.assertEqual(state_rowCntAfter - state_rowCntBefore, 1)
        # TEST if the city record was persisted to the database
        self.assertEqual(city_rowCntAfter - city_rowCntBefore, 1)

    def reset_conn(self):
        ''' Performs tear down and setup to
        create a new connection and cursor object.
        '''
        self.tearDown()
        self.setUp()
