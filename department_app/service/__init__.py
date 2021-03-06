# department_app/service/__init__.py
"""
This is the __init__.py file of service module.
Imports the departments and employees submodules
"""
# pylint: disable=cyclic-import
# local imports
from . import departments
from . import employees
