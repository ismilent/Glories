import os

class Config(object):
    HOST = '0.0.0.0'
    PORT = 8001
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@localhost:3007'
    SQLALCHEMY_CONNECT_OPTIONS = {}
    THREADS_PRE_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'secret'
    SECRET_KEY = 'secret'

class DevConfig(Config):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')