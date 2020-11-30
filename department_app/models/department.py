# department_app/models/department.py

# local imports
from department_app import db


class Department(db.Model):
    """
    Create a department table
    Fields:
        id: the unique identifier of the department, primary key
        name: the name of the department, unique
        description: the description of the department
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def json(self):
        """
        This method is used to return the department in json format
        :return: the department in json format
        """
        return {
            'id': self.id, 'name': self.name,
            'description': self.description
        }

    def __repr__(self):
        """
        The representation of the department
        :return: the string, representing the department by its name
        """
        return '<Department: {}>'.format(self.name)
