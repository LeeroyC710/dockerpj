from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import dare
from application.forms import DareForm, SubmitField
from flask_login import current_user
import requests, json


#-----------this should fetch all the data from the db in prizes models--------
'''@app.route('/')
@app.route('/home')
def home():
    dareData = dare.query.all()
    return render_template('home.html', title='Home', dare=dareData, form=form)
'''
#-----------create a path that allows connection with the front----------------- 
'''@app.route("/")
def dare():
    form 
'''
#------------users route manager still need to be worked on---------------------
'''@app.route("/")
def route_user():
    user_data = []
    for users in user:
        user_data = {"name": user.name, "email": user.email}
        user_data.append(user_data)
    senseless_print()
    return json(user_data), render_template('login.html', form=form)
'''
@app.route('/', methods=['GET','POST'])
def generator():

    form = DareForm()
    payload={'':''}

    if form.is_submitted():
        
       response = requests.post("http://service3:5003/").json()
       return render_template('home.html', form=form, data=response)
   
    if request.method=='GET':
       return render_template('dare.html', title= 'Dare', form=form)


#--------------this will help debugging whilst developing 
#if __name__=="__main__":
   # app.run(host ="0.0.0.0", debug=True, port=5000)
