import requests
import json
import pandas as pd


data = requests.get('https://www.googleapis.com/books/v1/volumes?q=tomintitle:keyes&key=AIzaSyBE-wVgVmGOvgsbLkETRPNc8yWgAiYDhnk.').json()

df = pd.DataFrame({
    'title': data['volumeInfo']['title'],
    'authors': data['volumeInfo']['authors'],
    'descriptions': data['volumeInfo']['description'],
    'categories': data['volumeInfo']['categories'],
})

print(df) 