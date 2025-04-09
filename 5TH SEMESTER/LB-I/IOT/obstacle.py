import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(24, False)
GPIO.output(25, False)
print('IR Sensor Ready.....')

try: 
    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            print('Object Detected')

            while GPIO.input(23):
                GPIO.output(25, True)  
                time.sleep(0.2)         
                GPIO.output(25, False) 
                time.sleep(0.2)         
        else:
            print('Object Not Detected')
            GPIO.output(24, False)
            GPIO.output(25, False)  

except KeyboardInterrupt:
    GPIO.cleanup()
