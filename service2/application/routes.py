from flask import Flask, jsonify, make_response
import sys
import requests
import random
import string
from application import app

@app.route('/', methods=['GET','POST'])
def random_letter():
    test = {"letter":"none"}
    random_letter = random.choice(string.ascii_letters[0:4])
    test['letter'] = random_letter
    return test

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5002)

