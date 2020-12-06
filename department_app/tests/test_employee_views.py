# department_app/tests/test_employee_views.py
"""
This module defines the test cases for employee views
"""
# pylint: disable=cyclic-import
# standard library imports
from datetime import datetime

# local imports
# pylint: disable=import-error
from department_app import db
from department_app.models.employee import Employee
from department_app.tests.test_base import BaseTestCase


class TestEmployeeViews(BaseTestCase):
    """
    This is the class for employee views test cases
    """
    def test_employees(self):
        """
        Tests whether the get request on employees page works correctly,
        returning the status code 200
        """
        response = self.app.get('/employees')
        self.assertEqual(200, response.status_code)

    def test_add_employee(self):
        """
        Tests whether the get request on add employee page works correctly,
        returning the status code 200
        """
        response = self.app.get('/employees/add')
        self.assertEqual(200, response.status_code)

    def test_employee_added(self):
        """
        Tests whether the get request on add employee page works correctly,
        and redirects to employees page, returning the status code 302
        """
        response = self.app.get('/employees/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_edit_employee(self):
        """
        Tests whether the get request on edit employee page works correctly,
        returning the status code 200
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/edit/1')
        self.assertEqual(200, response.status_code)

    def test_employee_edited(self):
        """
        Tests whether the get request on edit employee page works correctly,
        and redirects to employees page, returning the status code 302
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_delete_employee(self):
        """
        Tests whether the get request on delete employee page works correctly,
        returning the status code 200
        """
        date = datetime.strptime('02/23/1997', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=210, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/delete/1')
        self.assertEqual(302, response.status_code)
