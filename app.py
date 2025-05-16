from flask import Flask, jsonify
import time

app = Flask(__name__)
time_requests = 0

@app.route('/time')
def get_time():
    global time_requests
    time_requests += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": time_requests})
