# forms.py
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from email_validator import validate_email, EmailNotValidError

class SignUpForm(FlaskForm):
    fullname = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_email(form, field):
        try:
            v = validate_email(field.data)
            field.data = v.email
        except EmailNotValidError as e:
            raise ValidationError(str(e))
            
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PasswordForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
class FileForm(FlaskForm):
    file = FileField('Upload File', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditPasswordForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()], default='')
    name = StringField('Name', validators=[DataRequired()], default='')
    username = StringField('User Name', validators=[DataRequired()], default='')
    password = PasswordField('Password', validators=[DataRequired()], default='')

class EmailForm(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])
        def validate_email(form, field):
            try:
                v = validate_email(field.data)
                field.data = v.email
            except EmailNotValidError as e:
                raise ValidationError(str(e))
        submit = SubmitField('Submit')


class ChangePassForm(FlaskForm):

    password = PasswordField('Password1', validators=[DataRequired()])
    confirm_password = PasswordField('Password2', validators=[DataRequired()])
    submit = SubmitField('Submit')

