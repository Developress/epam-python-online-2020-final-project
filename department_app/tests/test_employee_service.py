from datetime import datetime

from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service import employees
from department_app.tests.test_base import BaseTestCase


class TestDepartmentService(BaseTestCase):
    def setUp(self):
        super(TestDepartmentService, self).setUp()

    def test_get_employees(self):
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(2, len(employees.get_employees()))

    def test_add_employee(self):
        employees.add_employee(name="Name", surname="surname", department_id=None, salary=200, date_of_birth='02/23/1990')
        self.assertEqual(1, Employee.query.count())

    def test_update_employee(self):
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
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        employees.delete_employee(1)
        self.assertEqual(0, Employee.query.count())

    def test_get_employees_born_on(self):
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(1, len(employees.get_employees_born_on("'02/23/1990'")))

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
        self.assertEqual(2, len(employees.get_employees_born_between("'05/15/1996'", "'05/20/1996'")))

    def test_get_employee_by_id(self):
        date = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee = Employee(name="name1", surname="surname1", salary=100, date_of_birth=date)
        db.session.add(employee)
        db.session.commit()
        self.assertEqual(1, employees.get_employee_by_id(1)['id'])