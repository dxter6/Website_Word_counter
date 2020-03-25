from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import g
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length
import os
import requests

#-------->flask-intilization<-------------------#
app = Flask(__name__,template_folder='templates')
Bootstrap(app)


#--------->Taking-unique-Key<-------------------#
app.secret_key = os.urandom(24)

#Index
@app.route('/')
def index():
    return render_template('index.html')
#Login
@app.route('/login')
def login():
    return render_template('login.html')
#Signup
@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')
#dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)
