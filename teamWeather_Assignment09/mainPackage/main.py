# Name: Kaileb strasser, Max Schiller, Josh Halbakken
# email: strassks@mail.uc.edu, schillmx@mail.uc.edu, halbakjc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024 
# Course/Section: IS-4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: this assignment calls and extracts data from the 
#openweather API and prints it to the console

# Brief Description of what this module does: this module calls the API key 
# Citations: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#https://www.instructables.com/Get-Weather-Data-Using-Python-and-Openweather-API/
# Anything else that's relevant: N/A



import requests
import json

if __name__ == "__main__":
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=58afbc2c63b8b7faf2d12f16b48ae8a4"
    city = input("What city would you like to know about? Enter here: ")
    
    response = requests.get(url.format(city))
    data = response.json()
    '''
    Pulls weather data from the city that is input
    @param url: The url and API key that is being called
    @return: weather data from openweather.org for the requested city
    '''
    if data["cod"] == "404": #error handling 
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
        
        