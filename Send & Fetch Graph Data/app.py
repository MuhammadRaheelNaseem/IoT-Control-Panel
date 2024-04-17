from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

data_history = {'labels': [], 'temperatures': [], 'humidity': []}

# API endpoint to receive DHT11 data and update data_history
@app.route('/api/update-dht-data', methods=['POST'])
def update_dht_data():
    global data_history

    dht_data = request.json
    temperature = dht_data.get('temperature')
    humidity = dht_data.get('humidity')

    if temperature is not None and humidity is not None:
        data_history['labels'].append(len(data_history['temperatures']))
        data_history['temperatures'].append(temperature)
        data_history['humidity'].append(humidity)

    return "Data received successfully!", 200

@app.route('/')
def index():
    return render_template('fetch_data.html')

@app.route('/api/get-graph-data', methods=['GET'])
def get_graph_data():
#     labels, temperatures, humidity = generate_dummy_data()
    dht_data = {"labels": data_history['labels'], "temperatures": data_history['temperatures'], "humidity": data_history['humidity']}
    print("Data Received Successfully")
    return jsonify(dht_data)

if __name__=="__main__":
    app.run(port=3000)
