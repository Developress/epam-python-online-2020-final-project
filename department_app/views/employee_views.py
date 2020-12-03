# department_app/views/department_views.py

# standard library imports
import json
import requests
import unicodedata

# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user
from ..service.departments import get_departments
from ..service.employees import get_employee_by_id


@user.route('/employees', methods=['GET', 'POST'])
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    if request.method == 'POST':
        if request.form['date']:
            params = {'date': "'" + str(request.form['date']) + "'"}
            employees = requests.get('http://localhost:5000/api/employees', params=params)
            flash(f"Success. Your employees born on {params['date']}:")
        else:
            params = {'start_date': "'" + str(request.form['start_date']) + "'",
                      'end_date': "'" + str(request.form['end_date']) + "'"}
            employees = requests.get('http://localhost:5000/api/employees', params=params)
            flash(f"Success. Your employees born between {params['start_date']} and {params['end_date']}:")

    else:
        # send a request to api
        employees = requests.get('http://localhost:5000/api/employees')

    employees = unicodedata.normalize('NFKD', employees.text).encode('ascii', 'ignore')
    # decode json
    employees = json.loads(employees)
    print(employees)
    return render_template('employees.html', title='Employees',
                           employees=employees)


@user.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    """
    This function represents the logic on /employees/add address
    :return: the rendered employee.html template to add a new employee
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at employee.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # send a request to api
        response = requests.post('http://localhost:5000/api/employees', params=request.form)
        # if operation ended successfully
        if response.status_code == 201:
            flash('You have successfully added a new employee.')
        else:
            # in case an error occurs
            flash('Error. Couldn\'t add an employee', 'error')

        # redirect to employees.html after the element is added or not
        return redirect(url_for('user.show_employees'))

    departments = {department['id']: department['name'] for department in get_departments()}
    roles = {role['id']: role['name'] for role in get_roles()}

    # load employee.html template
    return render_template('employee.html', add=add, title="Add Employee",
                           departments=departments, roles=roles)


@user.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    """
    This function represents the logic on /employees/edit address
    :return: the rendered employee.html template to edit an existing employee
    """
    # set add to False to display the 'Edit' title on employee.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        response = requests.put(f'http://localhost:5000/api/employees/{id}', params=request.form)
        # if name and description are defined
        if response.status_code == 200:
            flash('You have successfully updated the employee.')
        else:
            # in case an error occurs
            flash('Error. Couldn\'t update the employee', 'error')

        # redirect to employees.html after the element is updated or not
        return redirect(url_for('user.show_departments'))

    # get the employee to edit to show existing values
    employee = get_employee_by_id(id)

    departments = {department['id']: department['name'] for department in get_departments()}
    roles = {role['id']: role['name'] for role in get_roles()}
    # load employee.html template
    return render_template('employee.html', add=add, title="Add Employee",
                           employee=employee, departments=departments, roles=roles)


@user.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
    """
    This function represents the logic on /employees/delete address
    :return: the rendered employees.html template with deleted employee
    """
    requests.delete(f'http://localhost:5000/api/employees/{id}')
    flash('You have successfully deleted the employee.')

    # redirect to employees.html after the element is deleted
    return redirect(url_for('user.show_employees'))


def show_employees_born_on(date):
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    # send a request to api
    employees = requests.get('http://localhost:5000/api/employees', params=date)
    employees = unicodedata.normalize('NFKD', employees.text).encode('ascii', 'ignore')
    # decode json
    employees = json.loads(employees)
    print(employees)
    return render_template('employees.html', title='Employees',
                           employees=employees)