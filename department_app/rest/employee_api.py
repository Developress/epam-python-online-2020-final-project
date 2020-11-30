# department_app/rest/employee_api.py

# third-party imports
from flask import abort, jsonify
from flask_restful import reqparse, Resource

# local imports
from ..service import employees as employees_service

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('department_id')
parser.add_argument('role_id')
parser.add_argument('salary')
parser.add_argument('date_of_birth')


def abort_if_employee_doesnt_exist(id):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param id: the id of the resource
    """
    if employees_service.get_employee_by_id(id) not in employees_service.get_employees():
        abort(404, message="Employee {} doesn't exist".format(id))


class EmployeeList(Resource):
    """
    This is the class for EmployeeList Resource available at /employees url
    """

    def get(self):
        """
        This method is called when GET request is sent
        :return: the list of all employees in json format
        """
        return jsonify(employees_service.get_employees())

    def post(self):
        """
        This method is called when POST request is sent
        :return: the 'Employee added' response with status code 201
        """
        args = parser.parse_args()
        employees_service.add_employee(args['name'], args['department_id'],
                                       args['role_id'], args['salary'],
                                       args['date_of_birth'])
        return "Employee added", 201


class Employee(Resource):
    """
    This is the class for Employee Resource available at /employees/<id> url
    """

    def get(self, id):
        """
        This method is called when GET request is sent
        :return: the specific employee in json format
        """
        abort_if_employee_doesnt_exist(id)
        return jsonify(employees_service.get_employee_by_id(id))

    def put(self, id):
        """
        This method is called when PUT request is sent
        :return: the 'Employee updated' response with status code 200
        """
        args = parser.parse_args()
        employee = employees_service.get_employee_by_id(id)
        employees_service.update_employee(id, args.get('name', employee['name']),
                                          args.get('department_id', employee['department_id']),
                                          args.get('role_id', employee['role_id']), args.get('salary', employee['salary']),
                                          args.get('date_of_birth', employee['date_of_birth']))
        return "Employee updated", 200

    def delete(self, id):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_employee_doesnt_exist(id)
        employees_service.delete_employee(id)
        return '', 204
