import RPi.GPIO as GPIO
import time
import requests

THINGSPEAK_API_KEY = "20QJXBX5J4NXQBYQ"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def send_to_thingspeak(distance):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': distance
    }
    response = requests.get(THINGSPEAK_URL, params=payload)
    return response.status_code

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")

        status = send_to_thingspeak(dist)
        if status == 200:
            print("Data sent to ThingSpeak")
        else:
            print("Failed to send data")

        time.sleep(5)

except KeyboardInterrupt:
    print("Measurement stopped")
    GPIO.cleanup()