# department_app/models/employee.py

# local imports
from department_app import db
from .department import Department
from .role import Role


class Employee(db.Model):
    """
    Create an employee table
    Fields:
        id: the unique identifier of the employee, primary key
        name: the name of the employee
        department_id: the id of related department, foreign key to departments.id
        role_id: the id of related role, foreign key to roles.id
        salary: the salary of the employee
        date_of_birth: the date of birth of the employee
    """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    salary = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)

    def json(self):
        """
        This method is used to return the employee in json format
        :return: the employee in json format
        """
        return {
            'id': self.id, 'name': self.name,
            'department': Department.query.get_or_404(self.department_id).name,
            'role': Role.query.get_or_404(self.role_id).name,
            'salary': self.salary, 'date_of_birth': self.date_of_birth.strftime('%m/%d/%Y')
        }

    def __repr__(self):
        """
        The representation of the employee
        :return: the string, representing the employee by his name
        """
        return '<Employee: {}>'.format(self.name)
