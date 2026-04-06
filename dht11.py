#pip3 install adafruit-circuitpython-dht
#git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#cd Adafruit_Python_DHT
#sudo python3 setup.py install
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 18

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"Temp: {temperature}°C  Humidity: {humidity}%")
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(2)