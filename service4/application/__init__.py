from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY'] = 'yes'
#--------------------code for modelling databases check models.py-------------------------------------

from application import routes
