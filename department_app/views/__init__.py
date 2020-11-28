# department_app/views/__init__.py

# third-party imports
from flask import Blueprint

# local imports
from . import views

user = Blueprint('user', __name__)
