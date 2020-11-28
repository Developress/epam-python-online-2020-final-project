# department_app/views/views.py

# third-party imports
from flask import render_template

# local imports
from . import user


@user.route('/')
def homepage():
    """
    This function renders the homepage template on the / route
    :return: the rendered home.html template
    """
    return render_template('home.html', title='Welcome')


@user.route('/departments')
def show_departments():
    """
    This function renders the departments template on the /departments route
    :return: the rendered departments.html template
    """
    return render_template('departments.html', title='Departments')


@user.route('/roles')
def show_roles():
    """
    This function renders the roles template on the /roles route
    :return: the rendered roles.html template
    """
    return render_template('roles.html', title='Roles')


@user.route('/employees')
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    return render_template('employees.html', title='Employees')
