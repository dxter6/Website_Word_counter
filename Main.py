from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import g
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length
from wtforms import ValidationError
from werkzeug.security import generate_password_hash,check_password_hash
import os
import requests

#-------------->Os-database-environment<--------#

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#-------->flask-intilization<-------------------#
app = Flask(__name__,template_folder='templates')
Bootstrap(app)
#app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jesus/proj/edyst-challenge/Main/database.db'
db = SQLAlchemy(app)

# User calss
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


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
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                return redirect(url_for('dashboard'))
        return "<h1>Invalid Credientials</h1>"
        # return form.username.data+" "+form.password.data

    return render_template('login.html',form=form)

#Signup
@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,method='sha256')
        new_user = Users(username = form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user Created</h1>'
       # return form.username.data+" "+form.password.data+" "+form.email.data
    return render_template('signup.html',form=form)

#dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)
