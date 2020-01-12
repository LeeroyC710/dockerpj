from flask_wtf import FlaskForm 
from wtforms import SubmitField 

#-------------------------dare submit button-------------------------------
class DareForm(FlaskForm):
    submit = SubmitField('Lets Go!')

