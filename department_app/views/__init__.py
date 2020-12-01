# department_app/views/__init__.py

# third-party imports
from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__)

# local imports
from . import department_views
from . import role_views
from . import employee_views


@user.route('/')
def homepage():
    """
    This function renders the homepage template on the / route
    :return: the rendered home.html template
    """
    return render_template('home.html', title='Welcome')
