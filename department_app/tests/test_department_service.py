# department_app/tests/test_department_service.py
"""
This module defines the test cases for department service
"""
# pylint: disable=cyclic-import
# standard library imports
from datetime import datetime

# local imports
# pylint: disable=import-error
from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service import departments
from department_app.tests.test_base import BaseTestCase


class TestDepartmentService(BaseTestCase):
    """
    This is the class for department service test cases
    """
    def test_get_departments(self):
        """
        Adds 2 test records and tests whether the count of records is 2
        """
        department1 = Department(name="department1", description="description1")
        department2 = Department(name="department2", description="description2")
        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(departments.get_departments()))

    def test_add_department(self):
        """
        Adds a new department with specified parameters and tests whether the count
        of records is 1
        """
        departments.add_department(name="New department", description="New description")
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        """
        Adds a new department with specified parameters, updates it with new parameters
        and tests whether the values updated
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        departments.update_department(1, name="new name", description="new description")
        department = Department.query.get(1)
        self.assertEqual("new name", department.name)
        self.assertEqual("new description", department.description)

    def test_delete_department(self):
        """
        Adds a new department with specified parameters, deletes it and tests
        whether the count of records is 0
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        departments.delete_department(1)
        self.assertEqual(0, Department.query.count())

    def test_get_average_salary(self):
        """
        Adds a department and a few employees and tests whether the average salary
        has an expected value
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", department_id=1,
                             salary=100,date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", department_id=1,
                             salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(145, departments.get_average_salary(department.json()))

    def test_get_department_by_id(self):
        """
        Adds 1 test record and tests whether the id of added record is 1
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        self.assertEqual(1, departments.get_department_by_id(1)['id'])

    def test_department_representation(self):
        """
        Adds 1 test record and tests whether the string representation of
        department is correct
        :return:
        """
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        self.assertEqual('<Department: department1>', repr(department))
