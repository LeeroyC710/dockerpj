from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import random 
import string

#---------------prize generator function------------------------------
@app.route('/any_number', methods=[ 'POST'])
def any_number():
    chance = random.randint(0,25)
    prize = 0
    make_response = "You didn't win a prize"
    
    if chance >= 13
        prize = random.randint(0,25)
        resp = requests.get('http://notification:9000/notify').content    

    payload = request.get_json(force = True)
    payload["prize"] = prize
    make_response = requests.post("http://db-connector:5001/prizes/user_name", payload)

    return payload

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)
