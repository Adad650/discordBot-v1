import adafruit_dht
import board
import time

dhtDevice = adafruit_dht.DHT11(board.D4)  # D4 = GPIO4

def temp():

    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        return (f"Temp: {temperature}°C   Humidity: {humidity}%")
    except Exception as e:
        print("Reading failed, retrying...")

