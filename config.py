import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('RUBIK_API_SECRET_KEY', 'rubik_api_default_secret_key')
    DEBUG = False
    DATABASE_URI = ''
    LOG_SQL = False


class DevConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, './', 'rubik_api_dev.db')
    # DATABASE_URI = 'mysql://dev:dev321@localhost/almbic_test'
    LOG_SQL = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, './', 'rubik_api_test.db')


class ProdConfig(Config):
    DEBUG = False
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, './', 'rubik_api_prod.db')


config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

ACTIVATED_CONFIG = config_by_name[os.getenv('RUBIK_API_CONFIG') or 'dev']
