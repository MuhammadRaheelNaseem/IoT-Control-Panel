from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('slider.html')

@app.route('/api/slider-value', methods=['POST'])
def slider_value():
    slider_value = request.form['sliderValue']
    print("Slider Value:", slider_value)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run()
