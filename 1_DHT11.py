import Adafruit_DHT
import time

# Sensor type and pin configuration
sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f'Temp: {temperature}C  Humidity: {humidity}%')
    else:
        print('Failed to get reading. Try again!')
    time.sleep(2)