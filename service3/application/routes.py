from flask import Flask, jsonify, make_response
import sys
import requests
import string
import random
app = Flask(__name__)


@app.route('/', methods=['POST'])
def dare_generator():
    random_number = requests.post('http://service2:5001').text
    random_letter = requests.post('http://service1:5002').text
    if random_number.text=='0' and random_letter.text=='A': 
        return {"y0":"Number: 0, Letter: A, Dare: You have to avoid calling people by names for 5mins"} 
    elif random_number.text=='0' and random_letter.text=='B': 
        return {"y0":"Number: 0, Letter: B, Dare: Tell the next person that you have never ever met them"}
    elif random_number.text=='0' and random_letter.text=='C': 
        return {"y0":"Number: 0, Letter: C, Dare: Change the song playing to a classical song of you choice"}
    elif random_number.text=='0' and random_letter.text=='D':
        return {"y0":"Number: 0, Letter: D, Dare: 100push-ups in 5mins"}
    elif random_number.text=='1' and random_letter.text=='A': 
        return {"y0":"Number: 1, Letter: A, Dare: Tell everyone your most embarrassing moment"} 
    elif random_number.text=='1' and random_letter.text=='B': 
        return {"y0":"Number: 1, Letter: B, Dare: Eat a teaspoon of mustard"} 
    elif random_number.text=='1' and random_letter.text=='C': 
        return {"y0":"Number: 1, Letter: C, Dare: Dare someone of your choice"} 
    elif random_number.text=='1' and random_letter.text=='D':
        return {"y0":"Number: 1, Letter: D, Dare: Do 20 press-ups without stoping in 30secs"}
    elif random_number.text=='2' and random_letter.text=='A': 
        return {"y0":"Number: 2, Letter: A, Dare: Scream bogies very loud, right now!"} 
    elif random_number.text=='2' and random_letter.text=='B': 
        return {"y0":"Number: 2, Letter: B, Dare: Shout i love myself"} 
    elif random_number.text=='2' and random_letter.text=='C': 
        return {"y0":"Number: 2, Letter: C, Dare: Tell your friends you kissed Mariah Carey"}
    elif random_number.text=='2' and random_letter.text=='D': 
        return {"y0":"Number: 2, Letter: D, Dare: Have an arm-wrestling with the person sitting next to you!"}

#if __name__=='__main__':
   # app.run(debug=True, host='0.0.0.0', port=5003)
