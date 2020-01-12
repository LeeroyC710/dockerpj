from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from application.models import user, dare 


#-------------------------dare submit button-------------------------------
class DareForm(FlaskForm):
    submit = SubmitField('Lets Go!')

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
