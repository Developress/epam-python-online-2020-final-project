# department_app/views/__init__.py

# third-party imports
from flask import Blueprint

user = Blueprint('user', __name__)

# local imports
from . import views
