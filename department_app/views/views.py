# department_app/views/views.py

# third-party imports
from flask import render_template, request, redirect, url_for

# local imports
from . import user
from ..service import departments as departments_service
from ..service import roles as roles_service
from ..service import employees as employees_service


@user.route('/')
def homepage():
    """
    This function renders the homepage template on the / route
    :return: the rendered home.html template
    """
    return render_template('home.html', title='Welcome')


@user.route('/departments', methods=['GET', 'POST'])
def show_departments():
    """
    This function renders the departments template on the /departments route
    :return: the rendered departments.html template
    """
    departments = departments_service.list_departments()
    return render_template('departments.html', title='Departments',
                           departments=departments,
                           get_average_salary=departments_service.get_average_salary)


@user.route('/departments/add', methods=['GET', 'POST'])
def add_department():
    add = True

    if request.method == 'POST':
        name = request.form.get('name', '')
        description = request.form.get('description', '')
        if name and description:
            try:
                # add department to the database
                departments_service.add_department(name, description)
                print("Department added")
                # TODO add flash message success
            except:
                # in case department name already exists
                # TODO add flash message error
                print("Error")
                pass
            return redirect(url_for('user.show_departments'))

    # load department template
    return render_template('department.html', action="Add",
                           add=add, title="Add Department")


@user.route('/roles', methods=['GET', 'POST'])
def show_roles():
    """
    This function renders the roles template on the /roles route
    :return: the rendered roles.html template
    """
    roles = roles_service.list_roles()
    return render_template('roles.html', title='Roles',
                           roles=roles)


@user.route('/employees', methods=['GET', 'POST'])
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    employees = employees_service.list_employees()
    return render_template('employees.html', title='Employees',
                           employees=employees)
