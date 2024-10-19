import RPi.GPIO as GPIO
import time

sensor = 23  
buzzer = 24  
led = 25 

GPIO.setmode(GPIO.BCM)  
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

GPIO.output(buzzer, False)
GPIO.output(led, False)
print('IR Sensor Ready.....')

try: 
    while True:
        if GPIO.input(sensor):
            GPIO.output(buzzer, True)
            print('Object Detected')

            while GPIO.input(sensor):
                GPIO.output(led, True)  
                time.sleep(0.2)         
                GPIO.output(led, False) 
                time.sleep(0.2)         
        else:
            print('Object Not Detected')
            GPIO.output(buzzer, False)
            GPIO.output(led, False)  

except KeyboardInterrupt:
    GPIO.cleanup()
