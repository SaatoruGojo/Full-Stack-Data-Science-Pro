#5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask,render_template,request,session,url_for,redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    username = session.get('username', None)
    if username:
        username = session['username']
        return render_template('welcome.html',username = username)
    else:
        return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')