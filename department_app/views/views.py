# department_app/views/views.py

# third-party imports
from flask import flash, render_template, request, redirect, url_for

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
    """
    This function represents the logic on /departments/add address
    :return: the rendered department.html template to add a new department
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at department.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        description = request.form.get('description', '')

        # if name and description are defined
        if name and description:
            try:
                # add department to the database
                departments_service.add_department(name, description)
                flash('You have successfully added a new department.')
            except:
                # in case department name already exists
                flash('Error: department name already exists.', 'error')

            # redirect to departments.html after the element is added or not
            return redirect(url_for('user.show_departments'))

    # load department.html template
    return render_template('department.html', action="Add",
                           add=add, title="Add Department")


@user.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
def edit_department(id):
    """
    This function represents the logic on /departments/edit address
    :return: the rendered department.html template to edit an existing department
    """
    # set add to False to display the 'Edit' title on department.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        description = request.form.get('description', '')

        # if name and description are defined
        if name and description:
            try:
                # update department in the database
                departments_service.update_department(id, name, description)
                flash('You have successfully updated the department.')
            except:
                # in case department name already exists
                flash('Error. Couldn\'t update the department', 'error')

            # redirect to departments.html after the element is updated or not
            return redirect(url_for('user.show_departments'))

    # get the department to edit to show existing values
    department = departments_service.get_department_by_id(id)

    # load department.html template
    return render_template('department.html', action="Edit",
                           add=add, department=department, title="Edit Department")


@user.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
def delete_department(id):
    """
    This function represents the logic on /departments/delete address
    :return: the rendered departments.html template with deleted department
    """
    departments_service.delete_department(id)
    flash('You have successfully deleted the department.')

    # redirect to departments.html after the element is deleted
    return redirect(url_for('user.show_departments'))


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
