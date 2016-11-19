from flask_wtf import FlaskForm
from wtforms import (Field, StringField, BooleanField, PasswordField, FileField, HiddenField, DateField,
    SelectField, TextAreaField, IntegerField, RadioField, FieldList, FormField, SubmitField,
    DecimalField)
from wtforms.validators import Required, Optional, NumberRange, Email, EqualTo, NumberRange
from wtforms.fields.html5 import DecimalRangeField
from wtforms.widgets import TextInput

class LoginForm(FlaskForm):
  email    = StringField('Email', validators = [Required()])
  password = PasswordField('Password', validators = [Required()])
  remember = BooleanField('remember', default = False)

class SignUpForm(FlaskForm):
  email = StringField('Email', validators = [Required(), Email()]) 
  password = PasswordField('Password', validators = [Required(),
    EqualTo('confirm', message = 'Passwords must match')])
  confirm = PasswordField('Repeat Password')