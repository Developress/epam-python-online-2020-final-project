# department_app/tests/test_employee_service.py
"""
This module defines the test cases for employee service
"""
# pylint: disable=cyclic-import
# standard library imports
from datetime import datetime

# local imports
# pylint: disable=import-error
from department_app import db
from department_app.models.employee import Employee
from department_app.service import employees
from department_app.tests.test_base import BaseTestCase


class TestEmployeeService(BaseTestCase):
    """
    This is the class for employee service test cases
    """
    def test_get_employees(self):
        """
        Adds 2 test records and tests whether the count of records is 2
        """
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(2, len(employees.get_employees()))

    def test_add_employee(self):
        """
        Adds a new employee with specified parameters and tests whether the count
        of records is 1
        """
        employees.add_employee(name="Name", surname="surname", department_id=None,
                               salary=200, date_of_birth='02/23/1990')
        self.assertEqual(1, Employee.query.count())

    def test_update_employee(self):
        """
        Adds a new employee with specified parameters, updates it with new parameters
        and tests whether the values updated
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employees.update_employee(1, name="new name", surname="new surname", salary=200,
                                  department_id=None, date_of_birth='06/15/1990')
        employee = Employee.query.get(1)
        self.assertEqual("new name", employee.name)
        self.assertEqual("new surname", employee.surname)

    def test_delete_employee(self):
        """
        Adds a new employee with specified parameters, deletes it and tests
        whether the count of records is 0
        """
        date = datetime.strptime('02/23/1995', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=150, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employees.delete_employee(1)
        self.assertEqual(0, Employee.query.count())

    def test_get_employees_born_on(self):
        """
        Adds 2 test records and tests whether the search for employees born on specific
        date works correctly and the count of records is 1
        """
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(1, len(employees.get_employees_born_on("'02/23/1990'")))

    def test_get_employees_born_between(self):
        """
        Adds 3 test records and tests whether the search for employees born on specific
        date range works correctly and the count of records is 2
        """
        date1 = datetime.strptime('02/15/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1994', '%m/%d/%Y').date()
        date3 = datetime.strptime('05/19/1994', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=180, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=250, date_of_birth=date2)
        employee3 = Employee(name="name3", surname="surname3", salary=190, date_of_birth=date3)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.add(employee3)
        db.session.commit()
        self.assertEqual(2, len(employees.get_employees_born_between("'05/15/1994'",
                                                                     "'05/20/1994'")))

    def test_get_employee_by_id(self):
        """
        Adds 1 test record and tests whether the id of added record is 1
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        self.assertEqual(1, employees.get_employee_by_id(1)['id'])

    def test_employee_representation(self):
        """
        Adds 1 test record and tests whether the string representation of
        employee is correct
        :return:
        """
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        self.assertEqual('<Employee: name1 surname1>', repr(employee))
