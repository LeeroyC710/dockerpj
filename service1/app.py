from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import random 
import string

#---------------prize generator function------------------------------
@app.route('/any_number', methods=[ 'POST'])
def any_number():
    chance = random.randint(0,9)
    
    return chance

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)
