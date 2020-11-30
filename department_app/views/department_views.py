# department_app/views/department_views.py

# standard library imports
import json
import requests
import unicodedata

# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user
from ..service.departments import get_average_salary, get_department_by_id


@user.route('/departments', methods=['GET'])
def show_departments():
    """
    This function renders the departments template on the /departments route
    :return: the rendered departments.html template
    """
    # send a request to api
    departments = requests.get('http://localhost:5000/api/departments')
    departments = unicodedata.normalize('NFKD', departments.text).encode('ascii', 'ignore')
    # decode json
    departments = json.loads(departments)
    return render_template('departments.html', title='Departments',
                           departments=departments,
                           get_average_salary=get_average_salary)


@user.route('/departments/add', methods=['GET', 'POST'])
def add_department():
    """
    This function represents the logic on /departments/add address
    :return: the rendered department.html template to add a new department
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at department.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # send a request to api
        response = requests.post('http://localhost:5000/api/departments', params=request.form)
        # if operation ended successfully
        if response.status_code == 201:
            flash('You have successfully added a new department.')
        else:
            # in case department name already exists
            flash('Error: department name already exists.', 'error')

        # redirect to departments.html after the element is added or not
        return redirect(url_for('user.show_departments'))

    # load department.html template
    return render_template('department.html', add=add, title="Add Department")


@user.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
def edit_department(id):
    """
    This function represents the logic on /departments/edit address
    :return: the rendered department.html template to edit an existing department
    """
    # set add to False to display the 'Edit' title on department.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        response = requests.put(f'http://localhost:5000/api/departments/{id}', params=request.form)
        # if name and description are defined
        if response.status_code == 200:
            flash('You have successfully updated the department.')
        else:
            # in case department name already exists
            flash('Error. Couldn\'t update the department', 'error')

        # redirect to departments.html after the element is updated or not
        return redirect(url_for('user.show_departments'))

    # get the department to edit to show existing values
    department = get_department_by_id(id)

    # load department.html template
    return render_template('department.html', add=add,
                           department=department, title="Edit Department")


@user.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
def delete_department(id):
    """
    This function represents the logic on /departments/delete address
    :return: the rendered departments.html template with deleted department
    """
    requests.delete(f'http://localhost:5000/api/departments/{id}')
    flash('You have successfully deleted the department.')

    # redirect to departments.html after the element is deleted
    return redirect(url_for('user.show_departments'))
