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
@app.route("/users/")
def route_users():
    users_data = []
    for user in users:
        user_data = {"name": user.name, "email": user.email}
        users_data.append(user_data)
    senseless_print()
    return json(users_data)

@app.route('/', methods=['GET','POST'])
def service4():

    form = DareForm()
    generator=""

    if form.is_submitted():
        
       response = requests.post("http://service3:5003")

       if service4: 
           random_letter=service4.json()["random_letter"]
           random_number=service4.json()["random_number"]
           service4=service4.json()["service4"]
      
       #app.logger.info("***************************************")
       #app.logger.info(response)
       #generator = response.json()['d0']
       
       return render_template('home.html', random_letter=random_letter, random_number=random_number, service4=service4)

   # return render_template('home.html', title= 'Dare', form=form, generator=generator)


#--------------this will help debugging whilst developing 
#if __name__=="__main__":
   # app.run(host ="0.0.0.0", debug=True, port=5000)
