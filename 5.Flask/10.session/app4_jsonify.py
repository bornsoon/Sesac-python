from flask import Flask, session, request, json, jsonify, send_from_directory
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'this-is-another-my-secret-hahaha'

users = [
    {'name': 'Alice', 'id':'alice', 'pw':'alice'},
    {'name': 'Bob', 'id':'bob', 'pw':'bob1234'},
    {'name': 'Charlie', 'id':'charlie', 'pw':'hello'}
]

@app.route('/')     # CORS 문제 >> 임시방편
def home():
    return send_from_directory('static', 'index.html')
@app.route('/profile')
def profile():
    return send_from_directory('static', 'profile.html')

@app.route('/api/', methods=['POST'])
def api_login():

    #데이터를 json으로 처리해서 받아해야함
    data = request.json
    id = data.get('id')
    pw = data.get('pw')

    # 이 사용자가 목록에 있는지 검사
    user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
    print(user)

    if user:
        session['user'] = user # 로그인한 사용자 정보를 세션에 저장
        return jsonify({'status': 'succeess', 'message': '로그인에 성공하였습니다.'})    # profile은 함수명
    else:
        return jsonify({'status': 'error'}, {'message': '로그인에 실패하였습니다'})
    

@app.route('/api/profile/', methods=['GET', 'POST'])
def api_profile():
    user = session.get('user')   # 위에서 내가 저장한 것 다시 찾아오기
    
    error = None
    if request.method == 'POST':
        new_pw = request.form['new_password']

        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw
        
        # 나의 세션 변경 (해도 안해도 무방)
        user[id] = new_pw
        session['user'] = user

        return jsonify({'status': 'succeess'}, {'message': '비밀번호 변경에 성공하였습니다.'})

    return jsonify({'status': 'succeess'}, {'user': user})

@app.route('/api/logout')
def api_logout():
    session.pop('user', None) # 세션에서 사용자(user) 정보 삭제
    return jsonify({'status': 'success'}, {'message': '로그아웃 하였습니다.'}) # 로그아웃 이후 홈 페이지로 보내기

if __name__ == '__main__':
    app.run(debug=True)