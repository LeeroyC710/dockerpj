from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import string
import random
app = Flask(__name__)


@app.route('/', methods=(['POST'])
def prize_generator():
random_number = requests.post(http://service2:5000).text
random_letter = requests.post(http://service1:3000).text


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
