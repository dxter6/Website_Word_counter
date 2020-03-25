from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__,template_folder='templates')

#---------->Index page defining<-----------------#
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
#---------->user-Page-with-name<----------------#
@app.route('/user/<string:name>',methods=['GET'])
def user(name):
    if name:
        return render_template('user.html',name=name)
#---------->user-page-for-username-------------#
@app.route('/user/')
def users():
    return render_template('user.html')
 
#--------->submits-Page<-----------------------#
@app.route('/submits',methods=['GET'])
def submits():
    return render_template('submits.html')

#--------->Login-Page<-------------------------#
@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'abhinav' or request.form['password'] == 'abhinav@123':
            return render_template('user.html',name='abhinav')
        elif request.form['username'] == 'aneeq' or request.form['password'] == 'aneeq@123':
            return render_template('user.html',name='aneeq')
        elif  request.form['username'] == 'me' or request.form['password'] == 'me@123':
            return render_template('user.html',name='Me')
        else:
            error = "Invalid credientials Please try again"
    return render_template('login.html',error=error)



#--------->for-instat-app-running-&-debug<------#
if __name__ == "__main__":
    app.run(debug=True)
