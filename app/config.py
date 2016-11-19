import os
DEBUG =  True
_basedir = os.path.abspath(os.path.dirname(__file__))

# Forms and cookies
CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess" #needs new value
SECRET_KEY = 'values' #needs new value

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Use these for SQLALCHEMY_DATABASE_URI for MySQL or Postgres
# Replace "dbname" with your database name

# MySQL
#SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'mysql://root@localhost:8889/dbname')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Postgres
#SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'postgresql://localhost/dbname')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')