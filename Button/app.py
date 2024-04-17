from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('button.html')

@app.route('/api/led-on', methods=['GET','POST'])
def led_on():
    print({"status": "success", "message": "LED turned ON"})
    return jsonify({"status": "success", "message": "LED turned ON"})

@app.route('/api/led-off', methods=['GET','POST'])
def led_off():
    print({"status": "success", "message": "LED turned OFF"})
    return jsonify({"status": "success", "message": "LED turned OFF"})

@app.route('/api/relay-on', methods=['GET','POST'])
def relay_on():
    print({"status": "success", "message": "Relay turned ON"})
    return jsonify({"status": "success", "message": "Relay turned ON"})

@app.route('/api/relay-off', methods=['GET','POST'])
def relay_off():
    print({"status": "success", "message": "Relay turned OFF"})
    return jsonify({"status": "success", "message": "Relay turned OFF"})


if __name__ == '__main__':
    app.run()
