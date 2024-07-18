import requests
from dotenv import load_dotenv
import os

# 저 파일을 읽어서 메모리에 로딩한다
load_dotenv()

OWM_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

url = 'https://api.openweathermap.org/data/2.5/weather'  # EndPoint
params = {
    'q': 'Seoul', # q는 어쩌다보니 hidden api가 되었음...
    'appid': OWM_API_KEY,
    'units': 'metric', # 온도가 섭씨로 바뀜
    'lang': 'kr' # 기본값 en
}

response = requests.get(url, params=params)
response.raise_for_status()

weather_data = response.json()
city_name = weather_data['name']
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

print(f'도시: {city_name}')
print(f'온도: {temperature}')
print(f'날씨: {description}')