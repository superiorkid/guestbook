from wsgiref.validate import validator
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms import DataRequired, Email

class GuestForm(FlaskForm):
  name =StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email(granular_message=True)])
  message = TextAreaField('Messages', validators=[DataRequired()])
  captcha = RecaptchaField()
  submit = SubmitField('Submit')