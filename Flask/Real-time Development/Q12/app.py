#12. Build a Flask app that updates data in real-time using WebSocket connections.
# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update_data(data):
    # Broadcast the data to all connected clients
    socketio.emit('data_updated', data)

# Added a new route to manually trigger updates
@app.route('/trigger_update')
def trigger_update():
    # Manually trigger an update with sample data
    sample_data = "This is a manual update from the server!"
    socketio.emit('data_updated', sample_data)
    return 'Update triggered successfully!'

if __name__ == '__main__':
    # Run the application with SocketIO support
    socketio.run(app, debug=True)
