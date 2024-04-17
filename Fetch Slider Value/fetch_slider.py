import time
import requests

def get_slider_value():
    try:
        response = requests.get('http://127.0.0.1:3000/api/get-slider-value')
        data = response.json()
        return data
    except requests.exceptions.ConnectionError:
        print("Flask app is not running or unreachable.")
        return None

prev_slider_value = {"slider_value": None}

while True:
    slider_value = get_slider_value()

    if slider_value is not None and slider_value != prev_slider_value:
        print(f'Slider Data: {slider_value}')
        prev_slider_value = slider_value

    time.sleep(1)
