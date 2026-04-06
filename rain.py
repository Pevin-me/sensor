import time
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

while True:
    i = GPIO.input(channel)
    if i == 0:
        print('Raining')
        GPIO.output(26, 1)
        time.sleep(2)
    elif i == 1:
        print('No Rain')
        GPIO.output(26, 0)
        time.sleep(2)