import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

while True:
    GPIO.output(17,GPIO.HIGH)
    print('led on')
    GPIO.sleep(1)
    GPIO.output(17,GPIO.LOW)
    print('led off')
    GPIO.sleep(1)