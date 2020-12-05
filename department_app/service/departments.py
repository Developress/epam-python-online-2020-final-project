# department_app/service/departments.py
"""
This module defines crud operations to work with departments table
"""

# local imports
from department_app import db
from ..models.department import Department
from ..models.employee import Employee


def get_departments():
    """
    This function is used to select all records from departments table
    :return: the list of all departments
    """
    departments = Department.query.all()
    return [department.json() for department in departments]


def add_department(name, description):
    """
    This function is used to add a new department to departments table
    :param name: the name of the department
    :param description: the description of the department
    """
    department = Department(name=name, description=description)
    db.session.add(department)
    db.session.commit()


def update_department(id_, name, description):
    """
    This function is used to update an existing department
    :param id_: the id of the department to update
    :param name: the name of the department to update
    :param description: the description of the department to update
    """
    department = Department.query.get_or_404(id_)
    department.name = name
    department.description = description
    db.session.add(department)
    db.session.commit()


def delete_department(id_):
    """
    This function is used to delete an existing department
    :param id_: the id of the department to delete
    """
    department = Department.query.get_or_404(id_)
    db.session.delete(department)
    db.session.commit()


def get_average_salary(department):
    """
    This function is used to get average salary of the department
    :return: the average salary of the department
    """
    employees = Employee.query.filter_by(department_id=department['id']).all()
    # declare a variable for average salary
    average_salary = 0

    for employee in employees:
        # sum all the salaries from the department
        average_salary += employee.salary

    # calculate the average value
    if len(employees) > 0:
        average_salary /= len(employees)

    return average_salary


def get_department_by_id(id_):
    """
    This function is used to get the single department by id
    :param id_: the id of the department to get
    :return: the department with the specified id
    """
    department = Department.query.get(id_)
    return department.json() if department is not None else None
