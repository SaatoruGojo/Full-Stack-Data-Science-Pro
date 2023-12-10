# app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Dictionary to store connected clients
connected_clients = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    sid = request.sid
    print(f'Client connected: {sid}')

    # Store the client's SID in the dictionary
    connected_clients[sid] = True

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    print(f'Client disconnected: {sid}')

    # Remove the client's SID from the dictionary
    if sid in connected_clients:
        del connected_clients[sid]

@socketio.on('notify')
def handle_notify(data):
    recipient_sid = data['recipient_sid']
    message = data['message']

    # Check if the recipient exists before sending the notification
    if recipient_sid in connected_clients:
        # Send the notification to the specified recipient
        socketio.emit('notification', {'message': message}, room=recipient_sid)
    else:
        print(f'Recipient {recipient_sid} not found.')

if __name__ == '__main__':
    socketio.run(app, debug=False)
