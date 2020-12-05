# department_app/rest/__init__.py
"""
This is the __init__.py file of rest module.
Imports the department_api and employee_api submodules and registers the api links
"""
# third-party imports
from flask_restful import Api

# local imports
from . import department_api
from . import employee_api


def create_api(app):
    """
    This function is used to create the Api for the given app
    and add all the available resources
    :param app: the app to create Api for
    :return: the created api
    """
    api = Api(app)

    # adding the department resources
    api.add_resource(department_api.DepartmentList, '/api/departments')
    api.add_resource(department_api.Department, '/api/departments/<id_>')

    # adding the employee resources
    api.add_resource(employee_api.EmployeeList, '/api/employees')
    api.add_resource(employee_api.Employee, '/api/employees/<id_>')

    return api
