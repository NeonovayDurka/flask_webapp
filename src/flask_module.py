from flask import Flask, jsonify
import socket
from datetime import datetime
import os

app = Flask(__name__)
visit_count = 0

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def hello():
    global visit_count
    visit_count += 1
    return jsonify({
        "message": "Hello from Flask!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "visits": visit_count,
        "version": os.getenv('APP_VERSION', '1.0.0')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
