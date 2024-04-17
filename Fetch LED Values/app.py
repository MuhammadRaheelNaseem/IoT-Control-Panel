from flask import Flask, render_template, request, jsonify
import requests
import random, math, time
import threading

app = Flask(__name__)
led_state = 0

@app.route('/')
def index():
    return render_template('fetch_btn.html')

@app.route('/api/slider-value', methods=['POST'])
def slider_value():
    slider_value = request.form['sliderValue']
    slider_value_2 = {"status": "success", "message": "Slider value received", "value": slider_value}
    return jsonify(slider_value_2)

@app.route('/api/led-on', methods=['POST'])
def led_on():
    global led_state
    led_state = request.json['ledState']  # Accessing JSON data sent from the client
    led_on_value = {"status": "success", "message": "LED turned ON", "value": led_state}
    print(led_on_value)
    return jsonify(led_on_value)

@app.route('/api/led-off', methods=['POST'])
def led_off():
    global led_state
    led_state = 0
    led_state = request.json['ledState']  # Accessing JSON data sent from the client
    led_off_value = {"status": "success", "message": "LED turned OFF", "value": led_state}
    print(led_off_value)
    return jsonify(led_off_value)

@app.route('/api/led', methods=['POST'])
def update_led_state():
    global led_state
    led_state = request.form['ledState']
    data_1 = {"status": "success", "message": "LED state updated", "value": led_state}
    print(data_1)
    return jsonify(data_1)

@app.route('/api/get-led-state', methods=['GET'])
def get_led_state():
    global led_state
    x = {"led_state":led_state}
    return jsonify(x)

@app.route('/api/relay-on', methods=['POST'])
def relay_on():
    relay_on_value = {"status": "success", "message": "Relay turned ON", "value": 1}
    return jsonify(relay_on_value)

@app.route('/api/relay-off', methods=['POST'])
def relay_off():
    relay_off_value = {"status": "success", "message": "Relay turned OFF", "value": 0}
    return jsonify(relay_off_value)

        
if __name__ == '__main__':
    app.run(port=3000)
