# department_app/views/views.py

# standard library imports
from datetime import datetime

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
    return render_template('department.html', add=add, title="Add Department")


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
    return render_template('department.html', add=add,
                           department=department, title="Edit Department")


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


@user.route('/roles/add', methods=['GET', 'POST'])
def add_role():
    """
    This function represents the logic on /role/add address
    :return: the rendered role.html template to add a new role
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at role.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        description = request.form.get('description', '')

        # if name and description are defined
        if name and description:
            try:
                # add role to the database
                roles_service.add_role(name, description)
                flash('You have successfully added a new role.')
            except:
                # in case department name already exists
                flash('Error: role name already exists.', 'error')

            # redirect to roles.html after the element is added or not
            return redirect(url_for('user.show_roles'))

    # load role.html template
    return render_template('role.html', add=add, title="Add Role")


@user.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    """
    This function represents the logic on /roles/edit address
    :return: the rendered role.html template to edit an existing role
    """
    # set add to False to display the 'Edit' title on role.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        description = request.form.get('description', '')

        # if name and description are defined
        if name and description:
            try:
                # update role in the database
                roles_service.update_role(id, name, description)
                flash('You have successfully updated the role.')
            except:
                # in case role name already exists
                flash('Error. Couldn\'t update the role', 'error')

            # redirect to roles.html after the element is updated or not
            return redirect(url_for('user.show_roles'))

    # get the role to edit to show existing values
    role = roles_service.get_role_by_id(id)

    # load role.html template
    return render_template('role.html', add=add,
                           role=role, title="Edit Role")


@user.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    """
    This function represents the logic on /roles/delete address
    :return: the rendered roles.html template with deleted role
    """
    roles_service.delete_role(id)
    flash('You have successfully deleted the role.')

    # redirect to roles.html after the element is deleted
    return redirect(url_for('user.show_roles'))


@user.route('/employees/employees_born_on/<int:month>/<int:day>/<int:year>', methods=['GET', 'POST'])
def show_employees_born_on(month, day, year):
    date = datetime(year, month, day)
    employees = employees_service.get_employees_born_on(date)
    if employees.count() > 0:
        flash(f'Success. Your employees born on {month}/{day}/{year}:')
    else:
        flash('Sorry, the employees with such date of birth were not found(')
    return render_template('employees.html', title='Date search results', employees=employees)


@user.route('/employees', methods=['GET', 'POST'])
def show_employees():
    """
    This function renders the employees template on the /employees route
    :return: the rendered employees.html template
    """
    if request.method == 'POST':
        date = request.form.get('date', '')
        if date:
            month, day, year = date.split('/')
            return redirect(url_for('user.show_employees_born_on', month=month, day=day, year=year))

    employees = employees_service.list_employees()
    return render_template('employees.html', title='Employees', employees=employees)


@user.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    """
    This function represents the logic on /employees/add address
    :return: the rendered employee.html template to add a new employee
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at employee.html
    add = True

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        department_id = request.form.get('department', None)
        role_id = request.form.get('role', None)
        salary = request.form.get('salary', 0)
        date_of_birth = datetime.strptime(request.form.get('date_of_birth', ''), '%m/%d/%Y')
        print("----------------", name, department_id, role_id, salary, date_of_birth)
        # if name, salary and date of birth are defined
        if name and salary and date_of_birth:
            try:
                # add role to the database
                employees_service.add_employee(name, department_id, role_id,
                                               salary, date_of_birth)
                flash('You have successfully added a new employee.')
            except:
                # in case an error occurs
                flash('Error. Couldn\'t add an employee', 'error')

            # redirect to employees.html after the element is added or not
            return redirect(url_for('user.show_employees'))

    # load employee.html template
    departments = {department.id: department.name for department in departments_service.list_departments()}
    roles = {role.id: role.name for role in roles_service.list_roles()}
    return render_template('employee.html', add=add, title="Add Employee",
                           departments=departments, roles=roles)


@user.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    """
    This function represents the logic on /employees/edit address
    :return: the rendered employee.html template to edit an existing employee
    """
    # set add to False to display the 'Edit' title on employee.html
    add = False

    # if the user submits the form
    if request.method == 'POST':
        # get the values from the form
        name = request.form.get('name', '')
        department_id = request.form.get('department', None)
        role_id = request.form.get('role', None)
        salary = request.form.get('salary', 0)
        date_of_birth = datetime.strptime(request.form.get('date_of_birth', ''), '%m/%d/%Y')

        # if name, salary and date of birth are defined
        if name and salary and date_of_birth:
            try:
                # update employee in the database
                employees_service.update_employee(id, name, department_id, role_id,
                                                  salary, date_of_birth)
                flash('You have successfully updated the employee.')
            except:
                # in case an error occurs
                flash('Error. Couldn\'t update an employee', 'error')

            # redirect to employees.html after the element is updated or not
            return redirect(url_for('user.show_employees'))

    # get the employee to edit to show existing values
    employee = employees_service.get_employee_by_id(id)

    # load employee.html template
    departments = {department.id: department.name for department in departments_service.list_departments()}
    roles = {role.id: role.name for role in roles_service.list_roles()}
    return render_template('employee.html', add=add, employee=employee,
                           departments=departments, roles=roles,
                           title="Edit Employee")


@user.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
def delete_employee(id):
    """
    This function represents the logic on /employees/delete address
    :return: the rendered employees.html template with deleted employee
    """
    employees_service.delete_employee(id)
    flash('You have successfully deleted the employee.')

    # redirect to employees.html after the element is deleted
    return redirect(url_for('user.show_employees'))
