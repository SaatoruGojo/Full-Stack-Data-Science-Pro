#3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<username>')
def showProfile(username):
    return render_template('profile.html',username = username)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')