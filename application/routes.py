from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import prizes
#from application.forms import PrizesForm
from flask_login import current_user

#-----------this should fetch all the data from the db in prizes models--------
@app.route('/')
@app.route('/home')
def home():
    prizesData = prizes.query.all()
    return render_template('home.html', title='Home', prizes=prizesData)

#-----------create a path that allows connection with the front----------------- 
'''@app.route("/<path:path>")
def route_frontend(path): 
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

@app.route('/service4', methods=['Get','Post'])
def service4():
    response=requests.get("url randnumber")
    response1=requests.get("url randomletter")
    return render_template('.html', title= 'Prize', response=response.txt, response1=response1.txt)


#--------------this will help debugging whilst developing 
if __name__=="__main__":
    app.run(host ="0.0.0.0", debug=True, port=80)
