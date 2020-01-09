from flask_wtf import Flaskform 
from wtforms import StringField, SubmitField, PasswordField, BoolenField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from application.models import User, Dare 
from flask_login import LoginManager, current_user
from application import login_manager, db

#-------------------------dare submit button-------------------------------
class SubmitForm(FlaskForm):


    submit = SubmitField('lets Go!')

#-------------------------login form----------------------------------------
'''class LoginForm(FlaskForm):
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired()
                ]
        )

        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')'''

#--------------registration form------------------------------------------

'''class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=4, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')'''
