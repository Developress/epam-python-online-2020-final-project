# department_app/models/employee.py

# local imports
from department_app import db
from .department import Department


class Employee(db.Model):
    """
    Create an employee table
    Fields:
        id: the unique identifier of the employee, primary key
        name: the name of the employee
        surname: the surname of the employee
        department_id: the id of related department, foreign key to departments.id
        salary: the salary of the employee
        date_of_birth: the date of birth of the employee
    """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    salary = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)

    def json(self):
        """
        This method is used to return the employee in json format
        :return: the employee in json format
        """
        return {
            'id': self.id, 'name': self.name, 'surname': self.surname,
            'department': Department.query.get_or_404(self.department_id).name if self.department_id is not None else None,
            'salary': self.salary, 'date_of_birth': self.date_of_birth.strftime('%m/%d/%Y')
        }
