# Flask Base

This is a strong Flask base focusing on simplicity, while still having modern tooling and following best web practices.

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
yarn
```

### Running

```shell
# Python, serve the web app on localhost:5000
source venv/bin/activate
python run.py

# Livereload and SASS
gulp

# To recompile bundle.js (if you change app.js), run the following:
webpack app/static/js/app.js app/static/js/bundle.js

# If you change the models, you have to migrate and upgrade again:
python manage.py db migrate
python manage.py db upgrade
```

More coming soon