#2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/choose', methods=['POST'])
def choose():
    x = request.form.get('page')
    if x == 'about':
        return render_template('about.html')
    elif x == 'contact':
        return render_template('contact.html')
    elif x == 'blog':
        return render_template('blog.html')
    elif x == 'home':
        return render_template('index.html')  
    else:
        return render_template('index.html')  

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')
