# department_app/rest/__init__.py

# third-party imports
from . import department_api
from flask_restful import Api


def create_api(app):
    """
    This function is used to create the Api for the given app
    and add all the available resources
    :param app: the app to create Api for
    :return: the created api
    """
    api = Api(app)

    # adding the department resources
    api.add_resource(department_api.DepartmentList, '/departments')
    api.add_resource(department_api.Department, '/departments/<id>')

    return Api(app)
