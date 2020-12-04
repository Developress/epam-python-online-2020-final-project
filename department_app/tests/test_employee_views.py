from datetime import datetime
from department_app import db
from department_app.models.employee import Employee
from department_app.tests.test_base import BaseTestCase


class TestDepartmentViews(BaseTestCase):
    def setUp(self):
        super(TestDepartmentViews, self).setUp()

    def test_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(200, response.status_code)

    def test_add_employee(self):
        response = self.app.get('/employees/add')
        self.assertEqual(200, response.status_code)

    def test_employee_added(self):
        response = self.app.get('/employees/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_edit_employee(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/edit/1')
        self.assertEqual(200, response.status_code)

    def test_employee_edited(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_delete_employee(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/employees/delete/1')
        self.assertEqual(302, response.status_code)
