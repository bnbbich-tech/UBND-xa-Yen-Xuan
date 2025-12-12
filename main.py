from flask import Flask, render_template, request, jsonify, Response
from datetime import datetime
import json
import queue
import threading
import time

app = Flask(__name__)

# Quản lý clients SSE
clients = []
clients_lock = threading.Lock()

class SSEClient:
    def __init__(self):
        self.queue = queue.Queue()
        self.active = True
    
    def put(self, data):
        if self.active:
            try:
                self.queue.put_nowait(data)
            except queue.Full:
                pass

def add_client(client):
    with clients_lock:
        clients.append(client)

def remove_client(client):
    with clients_lock:
        client.active = False
        if client in clients:
            clients.remove(client)

conters = {
    1: {'current': 0, 'next': 1, 'served_today': 0, 'waiting_count': 0},
    2: {'current': 0, 'next': 1, 'served_today': 0, 'waiting_count': 0},
    3: {'current': 0, 'next': 1, 'served_today': 0, 'waiting_count': 0},
    4: {'current': 0, 'next': 1, 'served_today': 0, 'waiting_count': 0},
    5: {'current': 0, 'next': 1, 'served_today': 0, 'waiting_count': 0},
}

@app.route('/')
def index():
    return render_template('index.html', conters=conters)

@app.route('/admin')
def admin():
    return render_template('admin.html', conters=conters)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
