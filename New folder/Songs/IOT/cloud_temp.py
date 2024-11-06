import dht11
import RPi.GPIO as GPIO
import time
import requests
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
dht_sensor = dht11.DHT11(pin=16)
URL = 'https://api.thingspeak.com/update?api_key=6GEOZSBNXFHN2PV6&field1='

while True:
    try:
        result = dht_sensor.read()
        if result.is_valid():
            temperature = result.temperature
            humidity = result.humidity
            print(f"Humidity: {humidity:.2f}%")
            print(f"Temperature: {temperature:.2f}°C")
            newURL = URL + str(temperature) + '&field2=' + str(humidity)
            r = requests.get(newURL)
            print(f"Response from Thingspeak: {r.status_code}")
        else:
            print("Failed to retrieve data from sensor")
        
    except Exception as error:
        print(f"General error: {error}")
    
    finally:
        GPIO.cleanup()
    time.sleep(15)
