from flask import jsonify, abort
from flask_restful import Resource, reqparse

from ..service import departments as departments_service

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('description')


def abort_if_department_doesnt_exist(id):
    if departments_service.get_department_by_id(id) not in departments_service.get_departments():
        abort(404, message="Department {} doesn't exist".format(id))


class DepartmentList(Resource):
    def get(self):
        return jsonify({'Departments': departments_service.get_departments()})

    def post(self):
        args = parser.parse_args()
        departments_service.add_department(args['name'], args['description'])
        return "Department added", 201


class Department(Resource):
    def get(self, id):
        abort_if_department_doesnt_exist(id)
        return jsonify(departments_service.get_department_by_id(id))

    def delete(self, id):
        abort_if_department_doesnt_exist(id)
        departments_service.delete_department(id)
        return '', 204

    def put(self, id):
        args = parser.parse_args()
        department = departments_service.get_department_by_id(id)
        departments_service.update_department(id, args.get('name', department['name']),
                                              args.get('description', department['description']))
        return "Department updated", 201
