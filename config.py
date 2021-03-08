
from os import environ, path

class Config:
    """ Base Configuration Class """

class DevConfig(Config):
    """ Config for Development environment """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

""" Dictionary containing configuration objects for proper enviornment keys"""
app_config = {
    'development': DevConfig,
    'production': ProdConfig
}