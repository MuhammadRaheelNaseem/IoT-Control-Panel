import time
import requests

def get_button_state():
    response = requests.get('http://127.0.0.1:3000/api/get-led-state')
    data = response.json()
    return data

# Initialize the previous state to an initial value
prev_button_state = {"state": None}

while True:
    button_state = get_button_state()
    if button_state != prev_button_state:
        print(f'Button state: {button_state}')
        prev_button_state = button_state 

    time.sleep(1)  # Check the state every 1 second
