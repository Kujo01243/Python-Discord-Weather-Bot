##########################################################################
#Wetterabfrage über api
import requests
import json
from globale_funktionen import *

def getWeather(ort):
    serviceURL = "https://api.openweathermap.org/data/2.5/weather"
    requestStr = serviceURL + "?q=" + ort + "&units=metric&lang=de&appid=" + get_api()
    responseStr = requests.get(requestStr)

    jsonResponse = json.loads(responseStr.text)
    ortsname = jsonResponse['name']
    land = jsonResponse['sys']['country']
    temp = jsonResponse['main']['temp']
    pressure = str(jsonResponse['main']['pressure'])
    humidity = str(jsonResponse['main']['humidity'])
    lon = str(jsonResponse['coord']['lon'])
    lat = str(jsonResponse['coord']['lat'])
    cloud = jsonResponse['weather'][0]['description']
    windSpeed = str(jsonResponse['wind']['speed'])
    windDirection = str(jsonResponse['wind']['deg'])
    weatherid = str(jsonResponse['id'])
    returnwert = [ortsname, land, str(temp), pressure, humidity, cloud, windSpeed, windDirection, temp, weatherid]
    return returnwert



