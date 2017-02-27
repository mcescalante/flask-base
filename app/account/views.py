from app import app, lm, db
if app.config['USE_MAIL'] is True: from app import sp
from app.models import *
from app.forms import LoginForm, SignUpForm
from flask import render_template, flash, redirect, session, url_for, request, g, abort
from flask_login import login_user, logout_user, current_user, login_required
import json

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

accounts = Blueprint('accounts', __name__, template_folder='templates')

# Login, Signup, User functions

@accounts.route('/signup/', methods = ['GET', 'POST'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('index'))

  form = SignUpForm(request.form)
  if form.validate_on_submit():
    
    # Handle duplicate account creation, could be more elegant
    if User.query.filter_by(email=form.email):
      flash('Email already exists, try again', 'warning')
      return redirect(url_for('accounts.signup')) 
    
    user = User()
    form.populate_obj(user)
    user.createdOn = datetime.datetime.now()
    user.updatedOn = datetime.datetime.now()
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('Signed up successfully. Welcome!', 'success')
    return redirect(url_for('index'))

  return render_template('account/signup.html', title = 'Sign Up', form = form)


@accounts.route('/login/', methods= ['GET','POST'])
def login():
  # Already logged in; return to index
  if current_user.is_authenticated:
    return redirect(url_for('index'))

  # Not logged in; show the login form or errors
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email = form.email.data).first()
    if user is not None and user.valid_password(form.password.data):
      if login_user(user, remember = form.remember.data):
        session.permanent = not form.remember.data
        #Need to add proper message flashing code to base.html
        user.lastLoggedIn = datetime.datetime.now()
        db.session.commit()
        flash('Logged in successfully!', category = 'success')
        return redirect(request.args.get('next') or url_for('index'))
      else:
          flash('This username is disabled', 'danger')
    else:
        flash('Wrong username or password', 'danger')

  return render_template('account/login.html', title = 'Login', form = form)


@accounts.route('/logout/')
@login_required
def logout():
  logout_user()
  flash('Logged out successfully', 'success')
  return redirect(url_for('index'))

# Login manager configuration / customization
@lm.user_loader
def load_user(id):
  return User.query.get(int(id))

@lm.unauthorized_handler
def unauthorized():
    return abort(403)