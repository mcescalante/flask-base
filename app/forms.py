from flask_wtf import FlaskForm
from wtforms import (Field, StringField, BooleanField, PasswordField, FileField, HiddenField, DateField,
    SelectField, TextAreaField, IntegerField, RadioField, FieldList, FormField, SubmitField,
    DecimalField)
from wtforms.validators import DataRequired, Optional, NumberRange, Email, EqualTo, NumberRange
from wtforms.fields.html5 import DecimalRangeField
from wtforms.widgets import TextInput

class LoginForm(FlaskForm):
  email    = StringField('Email', validators = [DataRequired()])
  password = PasswordField('Password', validators = [DataRequired()])
  remember = BooleanField('remember', default = False)

class SignUpForm(FlaskForm):
  email = StringField('Email', validators = [DataRequired(), Email()]) 
  password = PasswordField('Password', validators = [DataRequired(),
    EqualTo('confirm', message = 'Passwords must match')])
  confirm = PasswordField('Repeat Password', validators= [DataRequired()])