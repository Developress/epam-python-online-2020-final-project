# department_app/tests/test_department_views.py
"""
This module defines the test cases for department views
"""
# pylint: disable=cyclic-import
# local imports
# pylint: disable=import-error
from department_app import db
from department_app.models.department import Department
from department_app.tests.test_base import BaseTestCase


class TestDepartmentViews(BaseTestCase):
    """
    This is the class for department views test cases
    """
    def test_homepage(self):
        """
        Tests whether the get request on homepage page works correctly,
        returning the status code 200
        """
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_departments(self):
        """
        Tests whether the get request on departments page works correctly,
        returning the status code 200
        """
        response = self.app.get('/departments')
        self.assertEqual(200, response.status_code)

    def test_add_department(self):
        """
        Tests whether the get request on add department page works correctly,
        returning the status code 200
        """
        response = self.app.get('/departments/add')
        self.assertEqual(200, response.status_code)

    def test_department_added(self):
        """
        Tests whether the get request on add department page works correctly,
        and redirects to departments page, returning the status code 302
        """
        response = self.app.get('/departments/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_edit_department(self):
        """
        Tests whether the get request on edit department page works correctly,
        returning the status code 200
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/edit/1')
        self.assertEqual(200, response.status_code)

    def test_department_edited(self):
        """
        Tests whether the get request on edit department page works correctly,
        and redirects to departments page, returning the status code 302
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_delete_department(self):
        """
        Tests whether the get request on delete department page works correctly,
        returning the status code 200
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/delete/1')
        self.assertEqual(302, response.status_code)
