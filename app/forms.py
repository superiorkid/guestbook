from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class GuestForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  message = TextAreaField('Messages', validators=[DataRequired()])
  recaptcha = RecaptchaField('Recapthha')
  submit = SubmitField('Submit')