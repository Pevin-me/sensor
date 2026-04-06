import RPi.GPIO as GPIO
import time

channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel):
        print('No Water Detected!')
        time.sleep(1)
    else:
        print('Water Detected!')
        time.sleep(1)