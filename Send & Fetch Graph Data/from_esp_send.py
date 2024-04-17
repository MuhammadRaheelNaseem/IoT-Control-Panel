import urequests as requests
import random
import time
import network
import gc
from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(15))

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("<YOUR SSID NAME>","<YOUR WIFI PASSWORD>")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
# Server URL to send the data
SERVER_URL = "http://alikhan029.pythonanywhere.com/api/update-dht-data"

def generate_random_data():
    # Generate random temperature and humidity values
#     temperature = random.uniform(30, 90)
#     humidity = random.uniform(40, 90)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return {"temperature": temp, "humidity": hum}

def send_dht_data_to_server(data):
    global SERVER_URL
    try:
        # Send the data to the server using a POST request
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the server.")
        else:
            print("Failed to send data to the server. Status code:", response.status_code)
        response.close()  # Close the connection to free memory
    except Exception as e:
        print("Error occurred while sending data to the server:", str(e))

if _name_ == "_main_":
    while True:
        try:
            # Generate random data
            dht_data = generate_random_data()
            # Send the data to the server
            send_dht_data_to_server(dht_data)
            # Free up memory
            gc.collect()
            # Wait for some time before sending the next data
            time.sleep(1)
        except KeyboardInterrupt:
            break
# Close the network connection when done
network.WLAN(network.STA_IF).disconnect()
