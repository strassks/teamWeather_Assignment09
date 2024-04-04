#weather_api.py
#Name: Kaileb strasser, Max Schiller, Josh Halbakken
# email: strassks@mail.uc.edu, schillmx@mail.uc.edu, halbakjc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024 
# Course/Section: IS-4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment calls and extracts data from the 
#openweather API and prints it to the console

# Brief Description of what this module does: This module defines the functions to run the data from the API
# Citations: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#https://www.instructables.com/Get-Weather-Data-Using-Python-and-Openweather-API/
# Anything else that's relevant: N/A
import requests

class WeatherAPI:
    """
    A class to interact with the OpenWeatherMap API to fetch weather information.
    """
    def __init__(self, api_key):
        self.api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
        self.api_key = api_key

    def get_weather_data(self, city):
        """
        Fetches weather data for a given city.

        :param city: City name for which the weather data is to be fetched.
        :return: A dictionary containing weather data.
        """
        response = requests.get(self.api_url.format(city, self.api_key))
        data = response.json()

        if data["cod"] == "404":
            return "City not found."
        else:
            return data

    def print_weather_data(self, city):
        """
        Fetches and prints weather data in a user-friendly format.

        :param city: City name for which the weather data is to be fetched and printed.
        """
        data = self.get_weather_data(city)
        
        if isinstance(data, str):  # If the data is a string, it indicates an error message.
            print(data)
        else:
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            temp = data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius

            print(f"Here is the weather for {city}:")
            print(f'Temperature: {round(temp, 2)} °C')
            print(f'Wind: {wind} m/s')
            print(f'Pressure: {pressure} hPa')
            print(f'Humidity: {humidity} %')
