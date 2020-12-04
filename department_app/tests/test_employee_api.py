import json
import unittest
from datetime import datetime

from department_app import db
from department_app.models.employee import Employee
from department_app.tests.test_base import BaseTestCase


class TestEmployeeApi(BaseTestCase):
    def setUp(self):
        super(TestEmployeeApi, self).setUp()

    def test_get_employees(self):
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        response = self.app.get('/api/employees')
        self.assertEqual(200, response.status_code)

    def test_get_employee(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.get('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_post_employee(self):
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

    def test_delete_department(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        response = self.app.delete('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_on(self):
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        response = self.app.get(f'/api/employees?date=\'02/23/1990\'')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_between(self):
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
        response = self.app.get(f'/api/employees?start_date=\'05/15/1990\'&end_date=\'05/20/1990\'')
        self.assertEqual(200, response.status_code)

    def test_abort_if_employee_doesnt_exist(self):
        response = self.app.delete('/api/employees/10')
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
