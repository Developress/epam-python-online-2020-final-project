# department_app/tests/test_employee_api.py
"""
This module defines the test cases for employee api
"""
# pylint: disable=cyclic-import
# standard library imports
import json
from datetime import datetime

# local imports
# pylint: disable=import-error
from department_app import db
from department_app.models.employee import Employee
from department_app.tests.test_base import BaseTestCase


class TestEmployeeApi(BaseTestCase):
    """
    This is the class for employee api test cases
    """
    def test_get_employees(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        works correctly, returning the status code 200
        """
        date1 = datetime.strptime('02/23/1993', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/25/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=230, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=160, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        response = self.app.get('/api/employees')
        self.assertEqual(200, response.status_code)

    def test_get_employee(self):
        """
        Adds 1 test record and tests whether the get request to /api/employees/<id>
        works correctly, returning the status code 200
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_post_employee(self):
        """
        Forms a json object and tests whether the post request to /api/employees
        works correctly, returning the status code 201
        """
        employee = {
            'name': 'name1',
            'surname': 'surname1',
            'salary': 100,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_put_employee(self):
        """
        Adds 1 test record, forms a json object and tests whether the put request to
        /api/employees/<id> works correctly, returning the status code 200
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employee = {
            'name': 'name1_updated',
            'surname': 'surname1_updated',
            'salary': 100,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete_employee(self):
        """
        Adds 1 test record and tests whether the delete request to /api/employees/<id>
        works correctly, returning the status code 200
        """
        date = datetime.strptime('02/15/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=400, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.delete('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_on(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        with date parameter (search for employees born on specific date) works
        correctly, returning the status code 200
        """
        date1 = datetime.strptime('05/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/20/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=120, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=250, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        response = self.app.get('/api/employees?date=\'05/23/1990\'')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_between(self):
        """
        Adds 3 test records and tests whether the get request to /api/employees
        with start_date and end_date parameters (search for employees born on specific date range)
        works correctly, returning the status code 200
        """
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        date3 = datetime.strptime('05/19/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        employee3 = Employee(name="name3", surname="surname3", salary=250, date_of_birth=date3)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.add(employee3)
        db.session.commit()
        response = self.app.get('/api/employees?start_date=\'05/15/1990\'&end_date=\'05/20/1990\'')
        self.assertEqual(200, response.status_code)

    def test_abort_if_employee_doesnt_exist(self):
        """
        Test whether the page aborts with status code 404 if there are no record with
        the specified id in the database
        """
        response = self.app.delete('/api/employees/10')
        self.assertEqual(404, response.status_code)

    def test_adding_none_values(self):
        """
        Forms a json object with none values and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': None,
            'surname': None,
            'salary': None,
            'date_of_birth': None
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_adding_empty_values(self):
        """
        Forms a json object with empty values and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': '',
            'surname': '',
            'salary': '',
            'date_of_birth': ''
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_adding_negative_salary(self):
        """
        Forms a json object with negative salary value and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': 'name1',
            'surname': 'surname1',
            'salary': -1,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_negative_salary(self):
        """
        Adds 1 test record, forms a json object with negative salary value values and tests
        whether the put request to /api/employees/<id> works correctly, returning the status code 400
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employee = {
            'name': 'name1_updated',
            'surname': 'surname1_updated',
            'salary': -1,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_empty_values(self):
        """
        Adds 1 test record, forms a json object with empty values and tests whether the
        put request to /api/employees/<id> works correctly, returning the status code 400
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employee = {
            'name': '',
            'surname': '',
            'salary': '',
            'date_of_birth': ''
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_none_values(self):
        """
        Adds 1 test record, forms a json object with none values and tests whether the
        put request to /api/employees/<id> works correctly, returning the status code 200
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employee = {
            'name': None,
            'surname': None,
            'salary': None,
            'date_of_birth': None
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_search_on_invalid_date(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        with invalid date parameter (search for employees born on specific date) works
        correctly, returning the status code 400
        """
        date1 = datetime.strptime('05/15/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('08/17/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=135, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=240, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        response = self.app.get('/api/employees?date=\'05/23/1990sdfdsafz\'')
        self.assertEqual(400, response.status_code)
