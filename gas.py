import RPi.GPIO as GPIO
import time

MQ135_PIN = 17 

GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ135_PIN, GPIO.IN)

while True:
        if GPIO.input(MQ135_PIN) == GPIO.LOW:
            print("Status: GAS DETECTED! [!] ")
        else:
            print("Status: Air is clear [OK]")
        
        time.sleep(1)

