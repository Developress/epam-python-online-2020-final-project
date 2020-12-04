import unittest
import tempfile

from department_app import create_app, db


class BaseTestCase(unittest.TestCase):
    """A basic test case"""
    def setUp(self):
        config_name = 'testing'
        app = create_app(config_name)
        self.test_db_file = tempfile.mkstemp()[1]
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.test_db_file
        with app.app_context():
            db.create_all()
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
