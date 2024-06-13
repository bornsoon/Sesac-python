from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'this-is-my-secret'  # 아무 문자열이나 쓰면 되고, 이게 실제로 세션 데이터를 저장하는 암호키로 사용됨.

@app.route('/')
def index():
    # 세션에 데이터 저장하기
    session['username'] = 'abcd1234'
    session['data'] = '1234'
    
    return '헬로우'

@app.route('/set_session/<value>')
def set_session_data(id):
    session['username'] = id
    
    return '데이터가 저장되었습니다.'

@app.route('/get_session')
def get_sesion_data():
    username = session.get('username', '없음')
    data = session.get('data', '데이터도 없음')
    
    return f'사용자이름: {username} 사용자데이터: {data}'

if __name__ == '__main__':
    app.run(debug=True)