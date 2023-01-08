#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
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

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', default='file') != 'db', 'file storage in use')
    def test_create_state(self):
        ''' Tests the creation of a State instance.
        '''
        cur = self.cursor

        # Prepare query
        qry = "SELECT * FROM states"

        # Execute query
        cur.execute(qry)

        # Get number of rows returned
        rowCntBefore = cur.rowcount

        # Add a record with the console
        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create State name="Lagos"')

        # Flush all remaining rows before next query
        #cur.fetchall()

        # Query database again
        self.tearDown()
        self.setUp()
        cur = self.cursor
        cur.execute(qry)

        # Get new row count
        rowCntAfter = cur.rowcount

        # TEST if the record was persisted to the database
        self.assertEqual(rowCntAfter - rowCntBefore, 1)
