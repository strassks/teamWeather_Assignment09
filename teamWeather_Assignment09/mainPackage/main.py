#main.py 
#Name: Kaileb strasser, Max Schiller, Josh Halbakken
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



from weather_api import WeatherAPI

if __name__ == "__main__":
    api_key = "58afbc2c63b8b7faf2d12f16b48ae8a4"  # Normally, you should avoid hardcoding the API key
    weather_api = WeatherAPI(api_key)
    city = input("What city would you like to know about? Enter here: ")
    weather_api.print_weather_data(city)