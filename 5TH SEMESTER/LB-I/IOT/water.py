import RPi.GPIO as GPIO         # Import library

# Initalize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(16, GPIO.IN)         # Set GPIO 16 as input for water level sensor signal
GPIO.setup(6, GPIO.OUT)         # Set GPIO 6 as output for LED

while True:
    if (GPIO.input(16)):
        GPIO.output(6, True)    # Turn ON LED if water detected
    else:
        GPIO.output(6, False)   # Keep LED OFF if no water detected

