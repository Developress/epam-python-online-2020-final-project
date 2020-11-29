# department_app/service/roles.py

# local imports
from department_app import db
from ..models.role import Role


def list_roles():
    """
    This function is used to select all records from roles table
    :return: the list of all roles
    """
    roles = Role.query.all()
    return roles


def add_role(name, description):
    """
    This function is used to add a new role to roles table
    :param name: the name of the role
    :param description: the description of the role
    """
    role = Role(name=name, description=description)
    db.session.add(role)
    db.session.commit()


def update_role(id, name, description):
    """
    This function is used to update an existing role
    :param id: the id of the role to update
    :param name: the name of the role to update
    :param description: the description of the role to update
    """
    role = Role.query.get_or_404(id)
    role.name = name
    role.description = description
    db.session.add(role)
    db.session.commit()


def delete_role(id):
    """
    This function is used to delete an existing role
    :param id: the id of the role to delete
    """
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()


def get_role_by_id(id):
    """
    This function is used to get the single role by id
    :param id: the id of the role to get
    :return: the role with the specified id
    """
    role = Role.query.get_or_404(id)
    return role
