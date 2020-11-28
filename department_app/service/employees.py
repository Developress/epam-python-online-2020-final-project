# department_app/service/employees.py

# local imports
from department_app import db
from ..models.employee import Employee


def list_employees():
    """
    This function is used to select all records from employees table
    :return: the list of all employees
    """
    employees = Employee.query.all()
    return employees


def add_employee(name, department_id, role_id, salary, date_of_birth):
    """
    This function is used to add a new employee to employees table
    :param name: the name of the employee
    :param department_id: the id of the related department
    :param role_id: the id of the related role
    :param salary: the salary of the employee
    :param date_of_birth: the date of birth of the employee
    """
    employee = Employee(name=name, department_id=department_id, role_id=role_id,
                        salary=salary, date_of_birth=date_of_birth)
    db.session.add(employee)
    db.session.commit()


def update_employee(id, name, department_id, role_id, salary, date_of_birth):
    """
    This function is used to update an existing employee
    :param id: the id of employee to update
    :param name: the name of the employee
    :param department_id: the id of the related department
    :param role_id: the id of the related role
    :param salary: the salary of the employee
    :param date_of_birth: the date of birth of the employee
    """
    employee = Employee.query.get_or_404(id)
    employee.name = name
    employee.department_id = department_id
    employee.role_id = role_id
    employee.salary = salary
    employee.date_of_birth = date_of_birth
    db.session.add(employee)
    db.session.commit()


def delete_employee(id):
    """
    This function is used to delete an existing employee
    :param id: the id of the employee to delete
    """
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()


def get_employees_born_on(date):
    """
    This function is used to get all the employees born on a specified date
    :param date: the date to filter with
    :return: the list of employees born on a specified date
    """
    employees = Employee.query.filter_by(date_of_birth=date)
    return employees


def get_employees_born_between(start_date, end_date):
    """
    This function is used to get all the employees born between specified end and start dates
    :param start_date: the date to start comparison with
    :param end_date: the date to end comparison with
    :return: the list of employees born between specified end and start dates
    """
    employees = Employee.query.filter_by(start_date < Employee.date_of_birth < end_date)
    return employees