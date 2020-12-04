# department_app/rest/department_api.py

# third-party imports
from flask import abort, jsonify, Response
from flask_restful import reqparse, Resource

# local imports
from ..service import departments as departments_service

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('description')


def abort_if_department_doesnt_exist(id):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param id: the id of the resource
    """
    if departments_service.get_department_by_id(id) is None:
        abort(Response("Department {} doesn't exist".format(id), 404))


class DepartmentList(Resource):
    """
    This is the class for DepartmentList Resource available at /departments url
    """
    def get(self):
        """
        This method is called when GET request is sent
        :return: the list of all departments in json format
        """
        return jsonify(departments_service.get_departments())

    def post(self):
        """
        This method is called when POST request is sent
        :return: the 'Department added' response with status code 201
        """
        args = parser.parse_args()
        departments_service.add_department(args['name'], args['description'])
        return "Department added", 201


class Department(Resource):
    """
    This is the class for Department Resource available at /departments/<id> url
    """
    def get(self, id):
        """
        This method is called when GET request is sent
        :return: the specific department in json format
        """
        abort_if_department_doesnt_exist(id)
        return jsonify(departments_service.get_department_by_id(id))

    def put(self, id):
        """
        This method is called when PUT request is sent
        :return: the 'Department updated' response with status code 200
        """
        args = parser.parse_args()
        department = departments_service.get_department_by_id(id)
        departments_service.update_department(id, args.get('name', department['name']),
                                              args.get('description', department['description']))
        return "Department updated", 200

    def delete(self, id):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_department_doesnt_exist(id)
        departments_service.delete_department(id)
        return 'Department deleted', 200
