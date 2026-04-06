import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while 1:
    if GPIO.input(23) == True:
        print('No Obstacle')
    if GPIO.input(23) == False:
        print('Alert!!! Obstacle')
    time.sleep(1)