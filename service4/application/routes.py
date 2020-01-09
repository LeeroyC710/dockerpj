from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import dare
#from application.forms import DareForm
from flask_login import current_user

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

    if form.validate_on_submit():
        
       response=requests.post("http://service3:5003/service3")
       generator = response.json()['y0']
    return render_template('home.html', title= 'Dare', generator=genarator, form=form)


#--------------this will help debugging whilst developing 
#if __name__=="__main__":
   # app.run(host ="0.0.0.0", debug=True, port=80)
