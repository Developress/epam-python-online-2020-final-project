from department_app import db
from department_app.models.department import Department
from department_app.tests.test_base import BaseTestCase


class TestDepartmentViews(BaseTestCase):
    def setUp(self):
        super(TestDepartmentViews, self).setUp()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_departments(self):
        response = self.app.get('/departments')
        self.assertEqual(200, response.status_code)

    def test_add_department(self):
        response = self.app.get('/departments/add')
        self.assertEqual(200, response.status_code)

    def test_department_added(self):
        response = self.app.get('/departments/add?added=true')
        self.assertEqual(302, response.status_code)

    def test_edit_department(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/edit/1')
        self.assertEqual(200, response.status_code)

    def test_department_edited(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/edit/1?edited=true')
        self.assertEqual(302, response.status_code)

    def test_delete_department(self):
        department = Department(name="department1", description="description1")
        db.session.add(department)
        db.session.commit()
        response = self.app.get('/departments/delete/1')
        self.assertEqual(302, response.status_code)
