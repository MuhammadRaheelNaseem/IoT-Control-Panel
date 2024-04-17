from flask import Flask, render_template, request, jsonify
import random, time

app = Flask(__name__)
slider_value = 0

@app.route('/')
def index():
    return render_template('fetch_slider.html')

@app.route('/api/slider-value', methods=['GET', 'POST'])
def update_slider_value():
    global slider_value
    if request.method == 'POST':
        slider_value = int(request.json['sliderValue'])  # Assume sliderValue is sent as JSON data
        message = "Slider value updated"
    else:
        message = "Slider value fetched"
    return jsonify({"status": "success", "message": message, "value": slider_value})

@app.route('/api/get-slider-value', methods=['GET'])
def get_slider_value():
    global slider_value
    return jsonify({"slider_value": slider_value})
  
if __name__ == '__main__':
    app.run(port=3000)
