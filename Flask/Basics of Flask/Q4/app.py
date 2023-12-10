#4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/display',methods=['POST'])
def showProfile():
    name = request.form.get("name")
    return render_template('display.html',name = name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')