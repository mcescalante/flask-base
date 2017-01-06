# Flask Base

This is a strong Flask base/boilerplate focusing on simplicity, while still having modern tooling and following best web practices.

### Features

- Always updated, production ready
- Basic User model with Login & Registration ready
- Blueprint ready (see `app/account` for sample)

#### Libraries

- **Flask:** Flask-SQLAlchemy, Flask-WTF, Flask-Login, Alembic/Flask-Migrate
- **JS & Frontend:** Bootstrap 4, Gulp, Livereload, and Webpack

### Setup (first time only)

```shell
# Python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Javascript & Frontend
npm i -g gulp webpack
yarn # or npm i

# Create js bundle
npm run buildjs
```

### Running

```shell
# Python, serve the web app on localhost:5000
source venv/bin/activate
python run.py

# Livereload and SASS
gulp

# To recompile bundle.js (if you change app.js), run the following:
npm run buildjs
# You can also run the actual webpack command itself if you prefer:
webpack app/static/js/app.js app/static/js/bundle.js

# If you change your database models, you have to migrate and upgrade again:
python manage.py db migrate
python manage.py db upgrade
```

### Deploying

In order to deploy, you need to move your entire application & database to a server or service (such as Heroku or Python Anywhere) and start it there.

Basic instructions for a VPS can be found in [a gist here](https://gist.github.com/mcescalante/5db616b9a826605f1df35f79b09cf6f6) but automated scripting & more will be coming soon.

More coming soon!