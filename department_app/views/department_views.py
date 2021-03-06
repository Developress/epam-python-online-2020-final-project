# department_app/views/department_views.py
"""
This module represents the logic on routes starting with /departments
"""
# pylint: disable=cyclic-import
# pylint: disable=unused-argument
# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user


@user.route('/departments', methods=['GET'])
def show_departments():
    """
    This function renders the departments template on the /departments route
    :return: the rendered departments.html template
    """
    return render_template('departments/departments.html', title='Departments')


@user.route('/departments/add', methods=['GET'])
def add_department():
    """
    This function represents the logic on /departments/add address
    :return: the rendered department.html template to add a new department
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at department.html
    add = True

    # get the added argument if the form is submitted
    added = request.args.get("added")

    if added is not None and added == 'true':
        # form a flash message
        flash('You have successfully added the department.')

        # redirect to departments.html after the element is added
        return redirect(url_for('user.show_departments'))

    if added is not None and added == 'false':
        # form a flash message
        flash('Couldn\'t add the department. Missing data', 'error')

        # redirect to department.html to enter the data again
        return redirect(url_for('user.add_department'))

    # load department.html template
    return render_template('departments/department.html', add=add, title="Add Department")


@user.route('/departments/edit/<int:id_>', methods=['GET'])
def edit_department(id_):
    """
    This function represents the logic on /departments/edit address
    :return: the rendered department.html template to edit an existing department
    """
    # set add to False to display the 'Edit' title on department.html
    add = False

    # get the edited argument if the form is submitted
    edited = request.args.get("edited")

    if edited is not None and edited == 'true':
        # form a flash message
        flash('You have successfully edited the department.')

        # redirect to departments.html after the element is edited
        return redirect(url_for('user.show_departments'))

    if edited is not None and edited == 'false':
        # form a flash message
        flash('Couldn\'t edit the department. Missing data', 'error')

        # redirect to department.html to enter the data again
        return redirect(url_for('user.edit_department', id_=id_))

    # load department.html template
    return render_template('departments/department.html', add=add, title="Edit Department")


@user.route('/departments/delete/<int:id_>', methods=['GET'])
def delete_department(id_):
    """
    This function represents the logic on /departments/delete address
    :return: the rendered departments.html template with deleted department
    """
    # form a flash message
    flash('You have successfully deleted the department.')

    # redirect to departments.html after the element is deleted
    return redirect(url_for('user.show_departments'))
