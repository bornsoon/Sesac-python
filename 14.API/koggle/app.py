from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('KAKAO_API_KEY')

def call_kakao_api(api_url, params):
    headers = {
        "Authorization": f"KakaoAK {API_KEY}"
    }
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    api_url_web = 'https://dapi.kakao.com/v2/search/web'
    api_url_img = 'https://dapi.kakao.com/v2/search/image'

    params = {
        "query": query,
        "sort": "accuracy", # 정확도순
        "page": 1,
        "size": 10
    }
    
    results_web = call_kakao_api(api_url_web, params)
    results_img = call_kakao_api(api_url_img, params)
    results = results_web.extend(results_img)
    return render_template('results.html', query=query, results=results)

if __name__=='__main__':
    app.run(debug=True)
