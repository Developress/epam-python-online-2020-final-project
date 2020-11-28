# department_app/service/departments.py

# local imports
from department_app import db
from ..models.department import Department
from ..models.employee import Employee


def list_departments():
    """
    This function is used to select all records from departments table
    :return: the list of all departments
    """
    departments = Department.query.all()
    return departments


def add_department(name, description):
    """
    This function is used to add a new department to departments table
    :param name: the name of the department
    :param description: the description of the department
    """
    department = Department(name=name, description=description)
    db.session.add(department)
    db.session.commit()


def update_department(id, name, description):
    """
    This function is used to update an existing department
    :param id: the id of the department to update
    :param name: the name of the department to update
    :param description: the description of the department to update
    """
    department = Department.query.get_or_404(id)
    department.name = name
    department.description = description
    db.session.add(department)
    db.session.commit()


def delete_department(id):
    """
    This function is used to delete an existing department
    :param id: the id of the department to delete
    """
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()


def get_average_salaries():
    """
    This function is used to get average salaries for all departments
    :return: the list of average salaries from all departments
    """
    # declare a list with average salaries
    average_salaries = []
    # get all the departments
    departments = list_departments()

    for department in departments:
        # get all the employees from a specified department
        employees = Employee.query.filter_by(department_id=department.id).all()
        # declare a variable for average salary
        average_salary = 0

        for employee in employees:
            # sum all the salaries from the department
            average_salary += employee.salary

        # calculate the average value
        average_salary /= len(employees)
        # append the average value to the list
        average_salaries.append(average_salary)

    return average_salaries

