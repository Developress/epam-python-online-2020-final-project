# department_app/tests/test_base.py
"""
This module defines a BaseTestCase class which will be a parent for all test cases
"""
# pylint: disable=cyclic-import
# standard library imports
import unittest
import tempfile

# local imports
# pylint: disable=import-error
from department_app import create_app, db


class BaseTestCase(unittest.TestCase):
    """
    The base class for the test case
    """
    def setUp(self):
        """
        This method is executed before every test case
        """
        # set the app configuration to testing
        config_name = 'testing'
        # create the app with the specified config
        app = create_app(config_name)
        # create a tempfile for database
        self.test_db_file = tempfile.mkstemp()[1]
        # specify the database connection string
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.test_db_file
        with app.app_context():
            db.create_all()
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        """
        This method is executed after every test case
        :return:
        """
        # close all the session and drop the tables
        db.session.close_all()
        db.drop_all()
