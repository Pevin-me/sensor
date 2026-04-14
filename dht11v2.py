pip3 install adafruit-circuitpython-dht


import time
import board
import adafruit_dht

dht_device = adafruit_dht.DHT11(board.D18, use_pulseio=False)

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        print(f"Temp: {temperature}°C  Humidity: {humidity}%")

    except RuntimeError as error:
        print(error)

    time.sleep(2)