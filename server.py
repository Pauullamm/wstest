from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

# Store chat messages
messages = []

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Send the chat history to the newly connected client
    emit('chat_history', messages, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send_message')
def handle_send_message(data):
    message = data['message']
    messages.append(message)  # Add the new message to the chat history
    emit('new_message', message, broadcast=True)
    emit('chat_history', messages, broadcast=True)  # Send the updated chat history

if __name__ == '__main__':
    socketio.run(app)

