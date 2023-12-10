from flask import Flask, render_template

app = Flask(__name__)

# Sample route to demonstrate 404 error
@app.route('/')
def index():
    return render_template('index.html')

# Custom error handler for 404 (Not Found) error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Custom error handler for 500 (Internal Server Error) error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
