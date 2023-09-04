from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
     """Welcome page"""

     return "welcome"


@app.route('/welcome/home')
def welcome_home():
     """Welcome home page"""

     return "welcome home"


@app.route('/welcome/back')
def welcome_back():
     """Welcome back page"""
     
     return "welcome back"