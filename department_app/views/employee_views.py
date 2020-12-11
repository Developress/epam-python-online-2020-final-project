# department_app/views/department_views.py
"""
This module represents the logic on routes starting with /employees
"""
# pylint: disable=cyclic-import
# pylint: disable=unused-argument
# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user


@user.route('/employees', methods=['GET'])
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    return render_template('employees/employees.html', title='Employees')


@user.route('/employees/add', methods=['GET'])
def add_employee():
    """
    This function represents the logic on /employees/add address
    :return: the rendered employee.html template to add a new employee
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at employee.html
    add = True

    # get the added argument if the form is submitted
    added = request.args.get("added")

    if added is not None and added == 'true':
        # form a flash message
        flash('You have successfully added the employee.')

        # redirect to employees.html after the element is added
        return redirect(url_for('user.show_employees'))
    elif added is not None and added == 'false':
        # form a flash message
        flash('Couldn\'t add the employee. Missing data', 'error')

        # redirect to employees.html after the element is added
        return redirect(url_for('user.add_employee'))

    # load employee.html template
    return render_template('employees/employee.html', add=add, title="Add Employee")


@user.route('/employees/edit/<int:id_>', methods=['GET'])
def edit_employee(id_):
    """
    This function represents the logic on /employees/edit address
    :return: the rendered employee.html template to edit an existing employee
    """
    # set add to False to display the 'Edit' title on employee.html
    add = False

    # get the edited argument if the form is submitted
    edited = request.args.get("edited")

    if edited is not None:
        # form a flash message
        flash('You have successfully edited the employee.')

        # redirect to employees.html after the element is edited
        return redirect(url_for('user.show_employees'))

    # load employee.html template
    return render_template('employees/employee.html', add=add, title="Edit Employee")


@user.route('/employees/delete/<int:id_>', methods=['GET', 'POST'])
def delete_employee(id_):
    """
    This function represents the logic on /employees/delete address
    :return: the rendered employees.html template with deleted employee
    """
    # form a flash message
    flash('You have successfully deleted the employee.')

    # redirect to employees.html after the element is deleted
    return redirect(url_for('user.show_employees'))
