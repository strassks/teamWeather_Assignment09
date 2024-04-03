# Name: Kaileb Strasser, Max Schiller







import requests
import json

if __name__ == "__main__":
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=58afbc2c63b8b7faf2d12f16b48ae8a4"
    city = input("What city would you like to know about? Enter here: ")
    
    response = requests.get(url.format(city))
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
    else:
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        temp = data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius

        print("Here is the weather for", city)
        print('Temperature:', round(temp, 2), '°C')
        print('Wind:', wind, 'm/s')
        print('Pressure:', pressure, 'hPa')
        print('Humidity:', humidity, '%')