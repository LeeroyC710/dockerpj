from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import string
app = Flask(__name__)

@app.route('/prize_gen_small', methods=['GET','POST'])
def prize_gen_small():
    chance = randint(0,100)
    prize = 0
    responds = "You didn't win a prize"

    if chance >= 50:
        prize = randint(1,10)
        responds = requests.get('http://notification:9000/notify').content

    payload = request.get_json(force = True)
    payload["prize"] = prize
    r = requests.post("http://db-connector:5001/user/user_name", payload)

    return payload


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)