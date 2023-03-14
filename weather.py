import requests
import json 
import pandas as pd 


city = input("Enter city name: ")
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=cb1657161a4c396d7510303571ee489f".format(city)).json()

df = pd.DataFrame({
    'city': data['name'],
    'country': data['sys']['country'],
    'temp': data['main']['temp'],
    'humidity': [data['main']['humidity']]
})

print(df)