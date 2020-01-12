from flask import Flask

app=Flask(__name__)
app.config['SECRET_KET'] = 'yes'
#--------------------code for modelling databases check models.py-------------------------------------

from application import routes
