#6. Build a Flask app that allows users to upload files and display them on the website
from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)

uploadFolder = 'uploads'
app.config['uploadFolder'] = uploadFolder

if not os.path.exists(uploadFolder):
    os.makedirs(uploadFolder)

@app.route('/')
def index():
    files = os.listdir(uploadFolder)
    return render_template('index.html',files = files)

@app.route('/upload', methods = ['POST'])
def upload():
    if 'files' not in request.files:
        return redirect(request.url)
    
    file = request.files['files']

    if file.filename=='':
        return redirect(request.url)

    file.save(os.path.join(app.config['uploadFolder'], file.filename))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)
