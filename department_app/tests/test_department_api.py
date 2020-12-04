# department_app/tests/test_department_api.py

# standard library imports
import json

# local imports
from department_app import db
from department_app.models.department import Department
from department_app.tests.test_base import BaseTestCase


class TestDepartmentApi(BaseTestCase):
    """
    This is the class for department api test cases
    """
    def setUp(self):
        """
        This method will be executed before every test case
        """
        super(TestDepartmentApi, self).setUp()

    def test_get_departments(self):
        """
        Adds 2 test records and tests whether the get request to /api/departments
        works correctly, returning the status code 200
        """
        department1 = Department(name="department1", description="description1")
        department2 = Department(name="department2", description="description2")
        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        response = self.app.get('/api/departments')
        self.assertEqual(200, response.status_code)

    def test_get_department(self):
        """
        Adds 1 test record and tests whether the get request to /api/departments/<id>
        works correctly, returning the status code 200
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/api/departments/1')
        self.assertEqual(200, response.status_code)

    def test_post_department(self):
        """
        Forms a json object and tests whether the post request to /api/departments
        works correctly, returning the status code 201
        """
        department = {
            'name': 'department1',
            'description': 'description1'
        }
        response = self.app.post('/api/departments',
                                 data=json.dumps(department),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_put_department(self):
        """
        Adds 1 test record, forms a json object and tests whether the put request to
        /api/departments/<id> works correctly, returning the status code 200
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        department = {
            'name': 'department1_update',
            'description': 'description1_update'
        }
        response = self.app.put('/api/departments/1',
                                data=json.dumps(department),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete_department(self):
        """
        Adds 1 test record and tests whether the delete request to /api/departments/<id>
        works correctly, returning the status code 200
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.delete('/api/departments/1')
        self.assertEqual(200, response.status_code)

    def test_abort_if_department_doesnt_exist(self):
        """
        Test whether the page aborts with status code 404 if there are no record with
        the specified id in the database
        """
        response = self.app.delete('/api/departments/10')
        self.assertEqual(404, response.status_code)
