from flask_wtf import Form
from wtforms import (Field, StringField, BooleanField, PasswordField, FileField, HiddenField, DateField,
    SelectField, TextAreaField, IntegerField, RadioField, FieldList, FormField, SubmitField,
    DecimalField)
from wtforms.validators import Required, Optional, NumberRange, Email, EqualTo, NumberRange
from wtforms.fields.html5 import DecimalRangeField
from wtforms.widgets import TextInput

class LoginForm(Form):
  email    = StringField('Email', validators = [Required()])
  password = PasswordField('Password', validators = [Required()])
  remember = BooleanField('remember', default = False)

class SignUpForm(Form):
  email = StringField('Email', validators = [Required(), Email()]) 
  password = PasswordField('Password', validators = [Required(),
    EqualTo('confirm', message = 'Passwords must match')])
  confirm = PasswordField('Repeat Password')