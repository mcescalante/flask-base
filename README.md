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
- **JS & Frontend:** Bootstrap 4, Gulp, Livereload, and Webpack

### Quick Setup

```shell
# Python
virtualenv venv
source venv/bin/activate
pip install -r requirements/base.txt

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

# Livereload and SASS
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
3. Execute either `pip install -r requirements.txt/mysql.txt` or `pip install -r requirements.txt/postgres.txt` (while inside virtual environment) to install the libraries needed for each respective database.

### Setting up mail
*Optional*

A lot of applications tend to use Flask-Mail and suggest to create a gmail address to send email with. While this works fine for small things, it isn't production-ready and Gmail doesn't exist to send transactional email (forgot password, confirm email, etc.). For this reason, my mail setup uses Sparkpost which has 100,000 emails per month for free. I am not sponsored or compensated in any way by Sparkpost. I have never exceeded this monthly limit, and the platform is rich and simple to use. It has reporting and other features that are great for real world applications.

1. Create an account on sparkpost.com
2. In your local environment, set the `SPARKPOST_API_KEY`:
    `export SPARKPOST_API_KEY='yourkeyhere'`
3. Update mail config variables in config.py 
4. All set!

If you use another transactional platform like Mandrill, it should be very simple to drop in here. Feel free to submit a PR with a new branch for any alternative email setups.

### Deploying

In order to deploy, you need to move your entire application & database to a server or service (such as Heroku or Python Anywhere) and start it there.

Basic instructions for a VPS can be found in [a gist here](https://gist.github.com/mcescalante/5db616b9a826605f1df35f79b09cf6f6) but automated scripting & more will be coming soon.

More coming soon!