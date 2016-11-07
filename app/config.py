import os

DEBUG =  True
CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess" #needs new value
SECRET_KEY = 'values' #needs new value

_basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False