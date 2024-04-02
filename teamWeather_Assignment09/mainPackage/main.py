import requests
import json
if __name__ == "__main__":
    response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    res = requests.get()
    data = res.json()
    
    city = input("What city would you like to know about? Enter here: ")
    
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    temp = data['main']['temp']
    
    print("here is the weather for ", city)
    print('Temperature:',temp,'°C')
    print('Wind:',wind)
    print('Pressure: ',pressure)
    print('Humidity: ',humidity)