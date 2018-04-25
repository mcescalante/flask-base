# Flask Base

This is a strong Flask base/boilerplate focusing on simplicity, while still having modern tooling and following best web practices.

![screenshot](https://mcescalante.com/flask-base.jpg)

### Table of Contents

- [Features](#features)
    - [Libraries](#libraries)
- [Quick Setup](#quick-setup)
- [Running](#running)
- Optional features
    - [Alternate Database](#database-configuration)
    - [Mail](#setting-up-mail)
- [Deploying](#deploying)

### Features

- Always updated, production ready, modern tooling
- Python 2 & 3 both supported and tested
- Basic User model with Login & Registration ready
- Blueprint ready (see `app/account` for sample)

#### Libraries

- **Flask:** Flask-SQLAlchemy, Flask-WTF, Flask-Login, Alembic/Flask-Migrate
- **JS & Frontend:** Bootstrap 4 (beta 2), Gulp, Livereload, and Webpack

### Quick Setup

```shell
# Python
pipenv install
pipenv shell

# Database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Javascript & Frontend
npm i -g gulp webpack
npm install # or yarn

# Create js bundle with webpack
npm run buildjs # non-minified
npm run buildprod # minified, prod-ready
```

### Running

```shell
# Python, serve the web app on localhost:5000
source venv/bin/activate
python run.py

# Livereload and SASS compilation
gulp

# To recompile bundle.js (if you change app.js), run one the following:
npm run buildjs # dev, unminified
npm run buildprod # prod, minified
# You can also run any actual webpack commands itself if you prefer or need to:
webpack app/static/js/app.js app/static/js/bundle.js

# If you change your database models, you have to migrate and upgrade again:
python manage.py db migrate
python manage.py db upgrade
```

### Database configuration
*Optional*

This boilerplate is ready for MySQL and Postgres, but uses sqlite by default. If you want to use something other than sqlite, you need to make a few small tweaks:

1. Create your database
2. In `app/config.py` you should comment the sqlite config line (11) and uncomment either mysql (19-20) or postgres (23-24). Make sure that you change the database name and add passwords or anything else you need to the connect string!
3. Execute either `pip install -r requirements/mysql.txt` or `pip install -r requirements/postgres.txt` (while inside virtual environment) to install the libraries needed for each respective database.

### Setting up mail
*Optional*

Removed for now.

### Deploying

In order to deploy, you need to move your entire application & database to a server or service (such as Heroku or Python Anywhere) and start it there.

Basic instructions for a VPS can be found in [a gist here](https://gist.github.com/mcescalante/5db616b9a826605f1df35f79b09cf6f6) but automated scripting & more will be coming soon.

More coming soon!