from flask import Flask, jsonify, make_response
import sys
import requests
import random
import string
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def random_letter():
    upper_alphabet = string.ascii_uppercase
    random_letter = random.choice(upper_alphabet[0:3])
    
    return random_letter

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)

