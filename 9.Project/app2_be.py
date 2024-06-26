from flask import Flask, jsonify, request
from database import get_stores, get_store_by_name

app = Flask(__name__)

# Web 서버를 대신해주는 코드..(지금은 웹서버가 없으니...)
@app.route('/')
def index():
    return app.send_static_file('index.html')  # static 폴더 안의 index.html


@app.route('/api/stores')
def api_stores():

    name = request.args.get('name')
    if name:
        stores = get_store_by_name(name)
    else:
        stores = get_stores()

    return jsonify(stores)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # 외부의 접속을 허용