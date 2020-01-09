from flask import Flask, jsonify, make_response
from application import app
import sys
import requests
import random
import string

#-------------- random number generator function------------------------------
@app.route('/', methods=['POST'])
def random_number():
    letsgo = {"number":"none"}
    chance = random.randint(0,3)
    letsgo['number'] = chance
    return letsgo

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5001) 