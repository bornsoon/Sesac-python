from flask import Flask, jsonify, request
from db_be import get_all, get_query_one, get_query
import math

app = Flask(__name__)   ## Flask(__name__, static folder="hello")로 static폴더명 변경하기
                        ## /static  <== 정적 리소스            /templete <== 템플릿 엔진

def pagings(category, str, page, per_page):
    total_page = math.ceil(len(category) / per_page)
    prePage = True if page < 8 else False
    nextPage = True if page < (total_page - 6) else False

    return {"category": str, "total": total_page, "pre": prePage, "next": nextPage }


@app.route('/')
@app.route('/user')
def home():
    return app.send_static_file('user_be.html')   # (루트 지정하지 않더라도) 루트에서는 기본으로 index.html으로 줌


@app.route('/api/user', methods=['GET', 'POST'])
@app.route('/api/user/<int:page>', methods=['GET', 'POST'])
def user(page=1):
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        name = request.form['name']
        arg = request.form['arg']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        name = request.args.get('name')
        arg = request.args.get('arg')

    if arg and name:
        query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%' AND gender = ?"
        params = (name.strip(), arg)
    else:
        if arg:
            query = "SELECT id, name, gender, age, birthdate FROM users WHERE gender = ?"
            name = ""
            params = (arg,)
        else:
            if not name:
                name = ""
            query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%'"
            arg = ""
            params = (name.strip(),)

    values = get_query(query, params)

    return jsonify({'values': values}, {'page': page}, {'name': name}, {'arg': arg})


if __name__ == '__main__':
    app.run(debug=True)