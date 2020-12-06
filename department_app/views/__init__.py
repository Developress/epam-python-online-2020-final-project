# department_app/views/__init__.py
"""
This is the __init__.py file of views module.
Imports the departments_views and employees_views submodules
Registers the user blueprint.
Specifies the logic on / address
"""
# pylint: disable=cyclic-import
# third-party imports
from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__)

# local imports
# pylint: disable=wrong-import-position
# disable wrong import positions because the blueprint must be
# registered before the views are imported
from . import department_views
from . import employee_views


@user.route('/')
def homepage():
    """
    This function renders the homepage template on the / route
    :return: the rendered home.html template
    """
    return render_template('home.html', title='Welcome')
