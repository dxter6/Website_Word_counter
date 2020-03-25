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

#Login form creation in FlaskForm
class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])
    remember = BooleanField('remember me')
#Registration form Creation in FlaskForm
class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(),Email(message='Invalid email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])
#--------->Taking-unique-Key<-------------------#
app.secret_key = os.urandom(24)

#Index
@app.route('/')
def index():
    return render_template('index.html')

#Login
@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html',form=form)

#Signup
@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()

    return render_template('signup.html',form=form)

#dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)
