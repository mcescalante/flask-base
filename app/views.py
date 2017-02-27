from app import app, lm, db
if app.config['USE_MAIL'] is True: from app import sp
from flask import render_template, flash, redirect, session, url_for, request, g, abort
from flask_login import login_user, logout_user, current_user, login_required
from .models import *
from .config import *
from .forms import *
import requests, json, time, datetime

# Needed for SVGs to be served with proper mimetype
import mimetypes
mimetypes.add_type('image/svg+xml', '.svg')


@app.route('/')
def index():
  # if not current_user.is_authenticated:
  #     return redirect(url_for('login'))
  return render_template('index.html', user = current_user)


# Redirects
def redirect_url(default='index'):
  return request.args.get('next') or \
         request.referrer or \
         url_for(default)


# Robots.txt & sitemap static route for indexing.
# Both files can be placed in app/static
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def sitemap():
  return send_from_directory(app.static_folder, request.path[1:])


# Error handlers
@app.errorhandler(404)
def page_not_found(error):
  return render_template('error/404.html'), 404

@app.errorhandler(403)
def page_not_found(error):
  return render_template('error/403.html'), 403