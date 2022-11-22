import weather
myLocation = "Madurai,IN"
APIKEY = "7a547a97f79ee73629edd98723ab36fe"

weatherData = weather.get(myLocation,APIKEY)
print ("WeatherData:",weatherData)
