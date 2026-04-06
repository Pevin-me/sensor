import RPi.GPIO as GPIO
import time

# Pin Configuration
GREEN_PIN = 17 
BLUE_PIN  = 27 

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

while True:
        # Green ON, Blue OFF
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        time.sleep(0.5) 

        # Green OFF, Blue ON
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.HIGH)
        time.sleep(0.5)
