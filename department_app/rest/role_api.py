# department_app/rest/role_api.py

# third-party imports
from flask import abort, jsonify
from flask_restful import reqparse, Resource

# local imports
from ..service import roles as roles_service

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('description')


def abort_if_role_doesnt_exist(id):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param id: the id of the resource
    """
    if roles_service.get_role_by_id(id) not in roles_service.get_roles():
        abort(404, message="Role {} doesn't exist".format(id))


class RoleList(Resource):
    """
    This is the class for RoleList Resource available at /roles url
    """
    def get(self):
        """
        This method is called when GET request is sent
        :return: the list of all roles in json format
        """
        return jsonify({'Roles': roles_service.get_roles()})

    def post(self):
        """
        This method is called when POST request is sent
        :return: the 'Role added' response with status code 201
        """
        args = parser.parse_args()
        roles_service.add_role(args['name'], args['description'])
        return "Role added", 201


class Role(Resource):
    """
    This is the class for Role Resource available at /roles/<id> url
    """
    def get(self, id):
        """
        This method is called when GET request is sent
        :return: the specific role in json format
        """
        abort_if_role_doesnt_exist(id)
        return jsonify(roles_service.get_role_by_id(id))

    def put(self, id):
        """
        This method is called when PUT request is sent
        :return: the 'Role updated' response with status code 200
        """
        args = parser.parse_args()
        role = roles_service.get_role_by_id(id)
        roles_service.update_role(id, args.get('name', role['name']),
                                  args.get('description', role['description']))
        return "Role updated", 200

    def delete(self, id):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_role_doesnt_exist(id)
        roles_service.delete_role(id)
        return '', 204
