import requests

url = 'https://www.example.com'

response = requests.get(url)  # 원하는 페이지를 요청

print(response.status_code)
print(response.text)