import dht11
import RPi.GPIO as GPIO
import time

def getTemperatureAndHumidity():
    def initTemperatureAndHumiditySensor():
        try:
            GPIO.setmode(GPIO.BCM)
            sensor = dht11.DHT11(pin=4)  # GPIO4 = physical pin 7
        except Exception as e:
            print ("error during sensor init")
            sensor = None

        return sensor

    def cleanupSensor(sensor):
        try:
            GPIO.cleanup()
        except Exception as e:
            print ("error during sensor cleanup")

    def getTemperatureAndHumidityOnce(sensor):
        t = 0
        h = 0

        try:
            result = sensor.read()
            if result.is_valid():
                t = result.temperature
                h = result.humidity
        except Exception as e:
            print ("received an error while reading values from the sensor")

        return (t, h)


    def trythis():
        s = initTemperatureAndHumiditySensor()
        if (s == None):
            print (" some error during sensor init. cannot continue")
            return

        T, H = getTemperatureAndHumidityOnce(s)
        cleanupSensor(s)
        print ("Temperature is: ", T, " and Humidity is: ", H)
        return (T, H)


    print ("hi there")
    trythis()
    print ("end of program")

'''
GPIO.setmode(GPIO.BCM)
sensor = dht11.DHT11(pin=4)  # GPIO4 = physical pin 7

try:
    while True:
        result = sensor.read()
        if result.is_valid():
            print(f"Temp: {result.temperature}°C   Humidity: {result.humidity}%")
        #else:
            #print("Failed to get reading, retrying...")
        time.sleep(2)
except KeyboardInterrupt:
'''