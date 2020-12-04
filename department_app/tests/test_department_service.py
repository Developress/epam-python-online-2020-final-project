from datetime import datetime

from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service import departments
from department_app.tests.test_base import BaseTestCase


class TestDepartmentService(BaseTestCase):
    def setUp(self):
        super(TestDepartmentService, self).setUp()

    def test_get_departments(self):
        department1 = Department(name="department1", description="description1")
        department2 = Department(name="department2", description="description2")
        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(departments.get_departments()))

    def test_add_department(self):
        departments.add_department(name="New department", description="New description")
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        departments.update_department(1, name="new name", description="new description")
        department1 = Department.query.get(1)
        self.assertEqual("new name", department1.name)
        self.assertEqual("new description", department1.description)

    def test_delete_department(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        departments.delete_department(1)
        self.assertEqual(0, Department.query.count())

    def test_get_average_salary(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        date1 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        date2 = datetime.strptime('05/16/1996', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", surname="surname1", department_id=1, salary=100, date_of_birth=date1)
        employee2 = Employee(name="name2", surname="surname2", department_id=1, salary=190, date_of_birth=date2)
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(145, departments.get_average_salary(department.json()))

    def test_get_department_by_id(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        self.assertEqual(1, departments.get_department_by_id(1)['id'])
