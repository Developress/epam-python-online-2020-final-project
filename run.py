# run.py
"""
This module creates a flask app with the given config by using the function create_app
defined in department_app package. It takes config from FLASK_CONFIG environmental
variable and runs the app on '0.0.0.0' host
"""

# standard library imports
import os

# local imports
from department_app import create_app

# specify the FLASK_CONFIG environmental variable before running the app firstly
# FLASK_CONFIG can be set to development, production or testing
config_name = os.getenv('FLASK_CONFIG')

# create the app with the specified config
app = create_app(config_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
