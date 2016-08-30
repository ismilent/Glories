DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_CONNECT_OPTIONS = {}

THREADS_PRE_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'secret'
SECRET_KEY = 'secret'