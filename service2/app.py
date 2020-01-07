from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import random
import string
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def random_letter():
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return l[random.randint(0,25)]
    responds = requests.get('http://notification:9000/notify').content

    payload = request.get_json(force = True)
    payload["letter"] = letter
    r = requests.post("http://db-connector:5001/user/user_name",payload)

print(random_letter())

    return payload


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)
