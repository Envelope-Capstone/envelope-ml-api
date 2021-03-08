from os import environ
from flask import Flask
from config import app_config

"""
Get the env file to configure current environment
"""

def init_app():
    """ Initialize Core components of the Flask API Application """
    app = Flask(__name__, instance_relative_config=False)

    # Get the environment the API is running in
    app_env = environ['FLASK_ENV']
    # Configure flask based on the environment variable in the .env file
    app.config.from_object(app_config[app_env])
    app.config.from_pyfile('../config.py')

    with app.app_context():
        # include the routes
        from .controllers.home import home_controller
        from .controllers.general_classification import general_classification_controller

        # register all blueprints
        app.register_blueprint(home_controller.home_bp)
        app.register_blueprint(general_classification_controller.general_classification_bp)

        return app
