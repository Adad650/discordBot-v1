import RPi.GPIO as GPIO
import dht11
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set GPIO pin for DHT11 data
DHT_PIN = 4

# Initialize DHT11 sensor
sensor = dht11.DHT11(pin=DHT_PIN)

def temp():
    result = sensor.read()
    if result.is_valid():
        return (f"Temp: {result.temperature}°C   Humidity: {result.humidity}%")
    else:
        return ("Reading failed, retrying...")


