import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

for i in range(0,10):
    GPIO.output(17,True)
    time.sleep(2)
    GPIO.output(17,False)
    print("LED:- 1")
    
    GPIO.output(22,True)
    time.sleep(2)
    GPIO.output(22,False)
    print("LED:- 2")
    
    GPIO.output(26,True)
    time.sleep(2)
    GPIO.output(26,False)
    print("LED:- 3")
    
    GPIO.output(27,True)
    time.sleep(2)
    GPIO.output(27,False)
    print("LED:- 4")
GPIO.cleanup()