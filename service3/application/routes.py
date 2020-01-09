from flask import Flask, jsonify, make_response, request
import sys
import requests
import string
import random
from application import app

@app.route('/', methods=['GET', 'POST'])
def dare_generator():
    if request.method == 'POST':
        random_number = requests.post('http://127.0.0.1:5001').json()
        random_letter = requests.post('http://127.0.0.1:5002').json()
        #return str(random_letter['letter']), str(random_number['number']) 
    #random_number['number']

        if str(random_number['number']) == '0' and str(random_letter['letter'])=='A': 
            return {"d0":"Number: 0, Letter: A, Dare: You have to avoid calling people by names for 5mins"} 
        elif str(random_number['number'])=='0' and str(random_letter['letter'])=='B': 
            return {"d0":"Number: 0, Letter: B, Dare: Tell the next person that you have never ever met them"}
        elif str(random_number['number'])=='0' and str(random_letter['letter'])=='C': 
            return {"d0":"Number: 0, Letter: C, Dare: Change the song playing to a classical song of you choice"}
        elif str(random_number['number'])=='0' and str(random_letter['letter'])=='D':
            return {"d0":"Number: 0, Letter: D, Dare: 100push-ups in 5mins"}
        elif str(random_number['number'])=='1' and str(random_letter['letter'])=='A': 
            return {"d0":"Number: 1, Letter: A, Dare: Tell everyone your most embarrassing moment"} 
        elif str(random_number['number'])=='1' and str(random_letter['letter'])=='B': 
            return {"d0":"Number: 1, Letter: B, Dare: Eat a teaspoon of mustard"} 
        elif str(random_number['number'])=='1' and str(random_letter['letter'])=='C': 
            return {"d0":"Number: 1, Letter: C, Dare: Dare someone of your choice"} 
        elif str(random_number['number'])=='1' and str(random_letter['letter'])=='D':
            return {"d0":"Number: 1, Letter: D, Dare: Do 20 press-ups without stoping in 30secs"}
        elif str(random_number['number'])=='2' and str(random_letter['letter'])=='A': 
            return {"d0":"Number: 2, Letter: A, Dare: Scream bogies very loud, right now!"} 
        elif str(random_number['number'])=='2' and str(random_letter['letter'])=='B': 
            return {"d0":"Number: 2, Letter: B, Dare: Shout i love myself"} 
        elif str(random_number['number'])=='2' and str(random_letter['letter'])=='C': 
            return {"d0":"Number: 2, Letter: C, Dare: Tell your friends you kissed Mariah Carey"}
        else:  
            return {"d0":"Number: 2, Letter: D, Dare: Have an arm-wrestling with the person sitting next to you!"}
    

#if __name__=='__main__':
   # app.run(debug=True, host='0.0.0.0', port=5003)
