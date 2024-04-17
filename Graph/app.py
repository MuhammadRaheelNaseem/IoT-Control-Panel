import random
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def generate_dummy_data():
    labels = [str(i) for i in range(1, 11)]  # Generate labels for 10 data points
    temperatures = [random.uniform(20, 30) for _ in range(10)]  # Random temperature readings
    humidity = [random.uniform(40, 70) for _ in range(10)]  # Random humidity readings
    return labels, temperatures, humidity

@app.route('/')
def index():
    return render_template('graph.html')

@app.route('/api/get-graph-data', methods=['GET'])
def get_graph_data():
    labels, temperatures, humidity = generate_dummy_data()
    return jsonify({"labels": labels, "temperatures": temperatures, "humidity": humidity})

if __name__ == '__main__':
    app.run()
