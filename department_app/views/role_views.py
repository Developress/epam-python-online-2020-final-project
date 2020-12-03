# department_app/views/role_views.py

# standard library imports
import json
import requests
import unicodedata

# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user


@user.route('/roles', methods=['GET'])
def show_roles():
    """
    This function renders the roles template on the /roles route
    :return: the rendered roles.html template
    """
    return render_template('roles/roles.html', title='Roles')


@user.route('/roles/add', methods=['GET'])
def add_role():
    """
    This function represents the logic on /roles/add address
    :return: the rendered role.html template to add a new role
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at role.html
    add = True

    # get the added argument if the form is submitted
    added = request.args.get("added")

    if added is not None:
        # form a flash message
        flash('You have successfully added the role.')

        # redirect to roles.html after the element is added
        return redirect(url_for('user.show_roles'))

    # load role.html template
    return render_template('roles/role.html', add=add, title="Add Role")


@user.route('/roles/edit/<int:id>', methods=['GET'])
def edit_role(id):
    """
    This function represents the logic on /roles/edit address
    :return: the rendered role.html template to edit an existing role
    """
    # set add to False to display the 'Edit' title on role.html
    add = False

    # get the edited argument if the form is submitted
    edited = request.args.get("edited")

    if edited is not None:
        # form a flash message
        flash('You have successfully edited the role.')

        # redirect to roles.html after the element is edited
        return redirect(url_for('user.show_roles'))

    # load role.html template
    return render_template('roles/role.html', add=add, title="Edit Role")


@user.route('/roles/delete/<int:id>', methods=['GET'])
def delete_role(id):
    """
    This function represents the logic on /roles/delete address
    :return: the rendered roles.html template with deleted role
    """
    # form a flash message
    flash('You have successfully deleted the role.')

    # redirect to roles.html after the element is deleted
    return redirect(url_for('user.show_roles'))
