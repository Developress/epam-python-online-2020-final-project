# department_app/views/views.py

# standard library imports
import json
import requests
import unicodedata
from datetime import datetime

# third-party imports
from flask import flash, render_template, request, redirect, url_for

# local imports
from . import user
from ..service import departments as departments_service
from ..service import roles as roles_service
from ..service import employees as employees_service

@user.route('/employees/employees_born_on/<int:month>/<int:day>/<int:year>', methods=['GET', 'POST'])
def show_employees_born_on(month, day, year):
    date = datetime(year, month, day)
    employees = employees_service.get_employees_born_on(date)
    if employees.count() > 0:
        flash(f'Success. Your employees born on {month}/{day}/{year}:')
    else:
        flash('Sorry, the employees with such date of birth were not found(')
    return render_template('employees.html', title='Date search results', employees=employees)


@user.route('/employees/employees_born_between/<int:month1>/<int:day1>/<int:year1>-/<int:month2>/<int:day2>/<int:year2>',
            methods=['GET', 'POST'])
def show_employees_born_between(month1, day1, year1, month2, day2, year2):
    start_date = datetime(year1, month1, day1)
    end_date = datetime(year2, month2, day2)
    employees = employees_service.get_employees_born_between(start_date, end_date)
    if employees.count() > 0:
        flash(f'Success. Your employees born on between {month1}/{day1}/{year1} and {month2}/{day2}/{year2}:')
    else:
        flash('Sorry, the employees with such dates of birth were not found(')
    return render_template('employees.html', title='Date search results', employees=employees)

