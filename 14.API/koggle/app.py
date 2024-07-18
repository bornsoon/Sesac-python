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
    search_type = request.args.get('type')

    if (search_type == 'web'):
        api_url = 'https://dapi.kakao.com/v2/search/web'
    elif (search_type == 'image'):
        api_url = 'https://dapi.kakao.com/v2/search/image'
    else:
        return "지원되지 않는 검색 타입입니다.", 400

    params = {
        "query": query,
        "sort": "accuracy", # 정확도순
        "page": 1,
        "size": 10
    }
    
    results = call_kakao_api(api_url, params)
    return render_template('results.html', query=query, results=results, search_type=search_type)

if __name__=='__main__':
    app.run(debug=True)
