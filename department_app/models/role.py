# department_app/models/role.py

# local imports
from department_app import db


class Role(db.Model):
    """
    Create a role table
    Fields:
        id: the unique identifier of the role, primary key
        name: the name of the role, unique
        description: the description of the role
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        """
        The representation of the role
        :return: the string, representing the role by its name
        """
        return '<Department: {}>'.format(self.name)
