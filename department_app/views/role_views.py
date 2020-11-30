# department_app/views/role_views.py

# standard library imports
import json
import requests
import unicodedata

# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user
from ..service.roles import get_role_by_id


@user.route('/roles', methods=['GET'])
def show_roles():
    """
    This function renders the roles template on the /roles route
    :return: the rendered roles.html template
    """
    # send a request to api
    roles = requests.get('http://localhost:5000/api/roles')
    roles = unicodedata.normalize('NFKD', roles.text).encode('ascii', 'ignore')
    # decode json
    roles = json.loads(roles)
    return render_template('roles.html', title='Roles',
                           roles=roles)


@user.route('/roles/add', methods=['GET', 'POST'])
def add_role():
    """
    This function represents the logic on /roles/add address
    :return: the rendered role.html template to add a new role
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at role.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # send a request to api
        response = requests.post('http://localhost:5000/api/roles', params=request.form)
        # if operation ended successfully
        if response.status_code == 201:
            flash('You have successfully added a new role.')
        else:
            # in case role name already exists
            flash('Error: role name already exists.', 'error')

        # redirect to roles.html after the element is added or not
        return redirect(url_for('user.show_roles'))

    # load role.html template
    return render_template('role.html', add=add, title="Add Role")


@user.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    """
    This function represents the logic on /roles/edit address
    :return: the rendered role.html template to edit an existing role
    """
    # set add to False to display the 'Edit' title on role.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        response = requests.put(f'http://localhost:5000/api/roles/{id}', params=request.form)
        # if name and description are defined
        if response.status_code == 200:
            flash('You have successfully updated the role.')
        else:
            # in case role name already exists
            flash('Error. Couldn\'t update the role', 'error')

        # redirect to roles.html after the element is updated or not
        return redirect(url_for('user.show_roles'))

    # get the department to edit to show existing values
    role = get_role_by_id(id)

    # load role.html template
    return render_template('department.html', add=add,
                           role=role, title="Edit Role")


@user.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    """
    This function represents the logic on /roles/delete address
    :return: the rendered roles.html template with deleted role
    """
    requests.delete(f'http://localhost:5000/api/roles/{id}')
    flash('You have successfully deleted the role.')

    # redirect to roles.html after the element is deleted
    return redirect(url_for('user.show_roles'))
