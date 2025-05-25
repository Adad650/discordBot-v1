import requests
from dotenv import load_dotenv
import os
import re

load_dotenv('mySecrets.env')
apiKey = os.getenv('API_KEY')

def getWeather(city):
    try:
        locationURL = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={apiKey}"
        response = requests.get(locationURL)
        data = response.json()
        if not data:
            return f"Couldn't find {city}."

        lat = data[0]['lat']
        lon = data[0]['lon']
        cityCountry = data[0]['country']
        cityName = data[0]['name']
        try:
            cityState = data[0]['state']
        except:
            cityState = ""

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&units=metric"
        response = requests.get(weather_url)
        data = response.json()

        temp = data['main']['temp']
        weatherDescription = data['weather'][0]['description']
        tempRound = round((float(temp)), 1)
        if cityState == "":
            returnStr = f"The weather for {cityName}, {cityCountry} is {tempRound} C and {weatherDescription}." 
        else:
            returnStr = f"The weather for {cityName}, {cityState}, {cityCountry} is {tempRound} C and {weatherDescription}." 
        return (returnStr)

    except Exception as e:
        return f"Error fetching weather: {e}"

if __name__ == "__main__":
    city = "London"
    print(getWeather(city))



