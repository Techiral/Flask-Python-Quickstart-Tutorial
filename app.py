#Techiral

''' Install required packages:-

pip install flask
Or
pip3 install -r requirements.txt

'''

#import required libraries
from flask import Flask

app = Flask(__name__)

#app routes
@app.route('/')
def home():
    return "Welcome To Flask Tutorial"

@app.route('/dash')
def dash():
    return "See the dashboard"

@app.route('/form')
def form():
    return "Give feedback"
