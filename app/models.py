from app import db
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import random, hashlib, base64

ROLE_USER = 0
ROLE_MANAGER = 1
ROLE_ADMIN = 2

class User(db.Model):
  '''
  This is the User model, which is based on information retrieved from the LDAP server
  upon successful login. Information is refreshed for various reasons, which are still being
  determined as of the initial testing release.
  '''
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  _password = db.Column('password', db.String(120), nullable = False)
  email = db.Column(db.String(120), nullable = False, index = True, unique = True)
  createdOn = db.Column(db.DateTime)
  updatedOn = db.Column(db.DateTime)
  lastLoggedIn = db.Column(db.DateTime)
  active = db.Column(db.SmallInteger, default = 1)
  fname = db.Column(db.String(120))
  lname = db.Column(db.String(120))
  active = db.Column(db.Boolean, default=True)
  role = db.Column(db.SmallInteger, default = ROLE_USER)

  def __repr__(self):
    return '<User %r>' % (self.username)

  def _set_password(self, password):
    self._password = generate_password_hash(password)

  def _get_password(self):
    return self._password

  password = db.synonym('_password', descriptor=property(_get_password, _set_password))

  def valid_password(self, password):
    return check_password_hash(self._password, password)

  def is_authenticated(self):
    return True

  def is_active(self):
    return self.active

  def user_status(self):
    return "Active" if self.active else "Deactivated"

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id) #python 2
    except NameError:
      return str(self.id) #python 3

  def is_administrator(self):
    return True if self.role == 2 else False