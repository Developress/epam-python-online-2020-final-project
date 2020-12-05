# config.py


class Config(object):
    """
    This is the class for common configurations across all environments
    """

    pass


class DevelopmentConfig(Config):
    """
    This is the class for development configurations
    """

    # Activates the debug mode on the app. This allows us to use the Flask debugger in case of
    # an unhandled exception, and also automatically reloads the application when it is updated.
    # It should however always be set to False in production. It defaults to False.
    DEBUG = True

    # setting this to True helps us with debugging by allowing SQLAlchemy to log errors.
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    This is the class for configurations across production environment
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    # Activates the testing mode of Flask extensions. This allows us to use testing properties
    # that could for instance have an increased runtime cost, such as unittest helpers.
    TESTING = True
    SQLALCHEMY_ECHO = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
