import requests
import random
import time
# import machine

# sensor = machine.Pin(15,machine.Pin.IN)
# Server URL to send the data
SERVER_URL = "http://127.0.0.1:3000/api/update-dht-data"
# SERVER_URL = "https://raheelapi.pythonanywhere.com/api/update-dht-data"

def generate_random_data():
    # Generate random temperature and humidity values
#     global sensor
#     sensor.measure()
#     temperature = sensor.temperature()
#     humidity = sensor.humidity()
    temperature = random.uniform(30, 90)
    humidity = random.uniform(40, 90)
    return {"temperature": temperature, "humidity": humidity}

def send_dht_data_to_server(data):
    global SERVER_URL
    try:
        # Send the data to the server using a POST request
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the server.")
        else:
            print("Failed to send data to the server. Status code:", response.status_code)
    except Exception as e:
        print("Error occurred while sending data to the server:", str(e))

if __name__ == "__main__":
    while True:
        # Generate random data
        dht_data = generate_random_data()
        # Send the data to the server
        send_dht_data_to_server(dht_data)
        # Wait for some time before sending the next data
        time.sleep(1)
