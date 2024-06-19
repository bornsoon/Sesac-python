from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)

# 사용자 DB
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 구현
        username = request.form['username']
        password = request.form['password']

        # 사용자 데이터를 내부 리스트DB에서 가져오기
        user_data = next((user for user in users if user['username'] == username), None)

        if user_data and user_data['password'] == password:
            session['user'] = username
            session.permanent = True
            print('패스워드 맞음!!')
            flash('로그인에 성공하였습니다.')    # 버퍼에 담김
            return redirect(url_for("home"))
        else:
            print('패스워드 틀림!!')
            # 메세지가 있으면 전달하고, 없으면 그냥 재 로그인
            flash('아이디/패스워드가 일치하지 않습니다.')
            return redirect(url_for("login"))
    
    else:
        # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:
            print('이전에 로그인 했음!!')
            return redirect(url_for("home"))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('로그아웃 되었습니다')                                  
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)