# department_app\__init__.py

# third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config  # dictionary, keys of which are names of config, and values - the appropriate classes

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    """
    This function creates an flask application with specified config
    :param config_name: can be development, production or testing
    :return: the created flask app
    """

    # Tells the app that configuration files are relative to the instance folder.
    # The instance folder is located outside the department_app package and can hold local data
    # that shouldn't be committed to version control, such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    @app.route('/')
    def hello():
        return render_template('home.html')

    return app
