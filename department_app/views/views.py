# department_app/views/views.py

# third-party imports
from flask import render_template

# local imports
from . import user
from ..service.departments import *
from ..service.roles import *
from ..service.employees import *


@user.route('/')
def homepage():
    """
    This function renders the homepage template on the / route
    :return: the rendered home.html template
    """
    return render_template('home.html', title='Welcome')


@user.route('/departments', methods=['GET', 'POST'])
def show_departments():
    """
    This function renders the departments template on the /departments route
    :return: the rendered departments.html template
    """
    departments = list_departments()
    average_salaries = get_average_salaries()
    return render_template('departments.html', title='Departments',
                           departments=departments, average_salaries=average_salaries)


@user.route('/roles', methods=['GET', 'POST'])
def show_roles():
    """
    This function renders the roles template on the /roles route
    :return: the rendered roles.html template
    """
    roles = list_roles()
    return render_template('roles.html', title='Roles',
                           roles=roles)


@user.route('/employees', methods=['GET', 'POST'])
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    employees = list_employees()
    return render_template('employees.html', title='Employees',
                           employees=employees)
