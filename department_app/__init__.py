# department_app/__init__.py

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
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

    # to create an api and register the routes
    from .rest import create_api
    api = create_api(app)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    # initialize the object for migrations
    migrate = Migrate(app, db)

    # initialize this to display flash messages
    Bootstrap(app)
    # needed import for initializing the db
    from department_app import models

    # register the user blueprint from views module
    from .views import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app
