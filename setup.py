from setuptools import find_packages
from setuptools import setup

setup(
    name='department_app',
    version='1.0.0',
    description='This application allows you to perform crud operations with employees and departments using rest api',
    author='Olena Hul',
    author_email='olena2002mik@gmail.com',
    url='https://gitlab.com/developress/epam-python-online-2020-final-project',
    install_requires=[
        'Flask>=1.1.2',
        'Flask-Bootstrap>=3.3.7.1',
        'Flask-Cors>=3.0.9',
        'Flask-Migrate>=2.5.3',
        'Flask-RESTful>=0.3.8',
        'Flask-SQLAlchemy>=2.4.4',
        'mysql-connector-python==8.0.22',
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages()
)
