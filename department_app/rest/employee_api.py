# department_app/rest/employee_api.py
"""
This module defines a rest interface to work with employees
"""
# pylint: disable=cyclic-import
# third-party imports
from flask import abort, jsonify, request, Response
from flask_restful import reqparse, Resource

# local imports
from ..service import employees as employees_service

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('surname')
parser.add_argument('department')
parser.add_argument('salary')
parser.add_argument('date_of_birth')


def abort_if_employee_doesnt_exist(id_):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param id_: the id of the resource
    """
    if employees_service.get_employee_by_id(id_) is None:
        abort(Response("Employee {} doesn't exist".format(id_), 404))


class EmployeeList(Resource):
    """
    This is the class for EmployeeList Resource available at /employees url
    """

    @staticmethod
    def get():
        """
        This method is called when GET request is sent
        :return: the list of all employees in json format
        """
        args = request.args

        if len(args) == 2:
            return jsonify(
                employees_service.get_employees_born_between(start_date=args['start_date'],
                                                             end_date=args['end_date']))
        if len(args) == 1:
            return jsonify(employees_service.get_employees_born_on(date=args['date']))

        return jsonify(employees_service.get_employees())

    @staticmethod
    def post():
        """
        This method is called when POST request is sent
        :return: the 'Employee added' response with status code 201
        """
        args = parser.parse_args()
        if args['name'] is None or args['surname'] is None or args['salary'] is None \
                or args['date_of_birth'] is None:
            abort(Response("Couldn't add employee. Missing data", 400))

        elif args['name'] == '' or args['surname'] == '' or args['salary'] == '' \
                or args['date_of_birth'] == '':
            abort(Response("Couldn't add employee. Missing data", 400))
        elif int(args['salary']) < 0:
            abort(Response("Salary must have a positive value", 400))
        else:
            employees_service.add_employee(args['name'], args['surname'],
                                           args['department'], args['salary'],
                                           args['date_of_birth'])
        return "Employee added", 201


class Employee(Resource):
    """
    This is the class for Employee Resource available at /employees/<id> url
    """

    @staticmethod
    def get(id_):
        """
        This method is called when GET request is sent
        :return: the specific employee in json format
        """
        abort_if_employee_doesnt_exist(id_)
        return jsonify(employees_service.get_employee_by_id(id_))

    @staticmethod
    def put(id_):
        """
        This method is called when PUT request is sent
        :return: the 'Employee updated' response with status code 200
        """
        args = parser.parse_args()
        employee = employees_service.get_employee_by_id(id_)
        employees_service.update_employee(id_, args.get('name', employee['name']),
                                          args.get('surname', employee['surname']),
                                          args.get('department', employee['department']),
                                          args.get('salary', employee['salary']),
                                          args.get('date_of_birth', employee['date_of_birth']))
        return "Employee updated", 200

    @staticmethod
    def delete(id_):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_employee_doesnt_exist(id_)
        employees_service.delete_employee(id_)
        return 'Employee deleted', 200
