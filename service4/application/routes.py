from flask import render_template, redirect, url_for, request
from application import app
from application.models import dare
from application.forms import DareForm, SubmitField
from flask_login import current_user
import requests, json

#------------------       Main_Service Handling Service3             --------------------------

@app.route('/', methods=['GET','POST'])
def generator():

    form = DareForm()
    payload={'':''}

    if form.is_submitted():
        
       response = requests.post("http://service3:5003/").json()
       return render_template('home.html', form=form, data=response)
   
    if request.method=='GET':
       return render_template('dare.html', title= 'Dare', form=form)



