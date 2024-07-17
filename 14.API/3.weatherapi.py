import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Seoul', # q는 어쩌다보니 hidden api가 되었음...
    'appid': 'e21a62c33e1ffbaa9a4d32ad8a6f6295'
}

response = requests