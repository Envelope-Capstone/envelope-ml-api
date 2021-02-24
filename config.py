
from os import environ, path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, ".env"))

class Config:
    """ Base Configuration Class """
    SECRET_KEY = environ['SECRET_KEY']

class DevConfig(Config):
    """ Config for Development environment """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


""" Dictionary containing configuration objects for proper enviornment keys"""
app_config = {
    'development': DevConfig
}