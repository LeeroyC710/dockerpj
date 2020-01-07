from flask import Flask, jsonify, make_response
import sys
import requests
import randint
import random
import string
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def random_prize():
    l = ['Apple','Boattrip','Cashprize','DayOut','EveningMeal','FoodGroceries','GenuineLeather','HouseOnTheHills','IvoryNecklace']
    return l[random.randint(0,9)]
    responds = requests.get('http://notification:9000/notify').content

    payload = request.get_json(force = True)
    payload["prize"] = letter
    r = requests.post("http://db-connector:5001/user/user_name",payload)

print(random_letter())

    return payload


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9019)
