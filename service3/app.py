from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import string
import random
app = Flask(__name__)


@app.route('/', methods=(['POST'])  
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


