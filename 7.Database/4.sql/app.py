from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)

# 사용자 DB
DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 행을 sqlite3.Row라는 객체 타입으로 반환
                                    #이걸 설정하면 각 Row의 결과는 Dict유형으로 반환됨.
    return conn

def init_db():
    with app.app_context():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)
        ''')

        # 기본 계정 추가  - 계정이 비어있을 때만...
        cur.execute("SELECT COUNT(*) as count FROM users")
        count = cur.fetchone()["count"]
        # count = cur.fetchone()[0]  # 이건 Row 타입이 아닌 기본값 (즉 튜플로) 반납될 때..
        if count == 0:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user1', 'password1'))
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user2', 'password2'))
            conn.commit()

        #데이터 조회
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print('-' * 30)
        for row in rows:
            print(row['id'], row['username'], row['password']) # 열 이름을 사용(Dict)해서 접근 가능함
        print('-' * 30)

        conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username, ))
        user_data = cur.fetchone()
        print(f'조회된 사용자: ', user_data)
        conn.close()

        if user_data and user_data['password'] == password:
            session['user'] = username
            session.permanent = True
            print('패스워드 맞음!!')
            return redirect(url_for("home"))
        else:
            print('패스워드 틀림!!')

            return redirect(url_for("login"))
    
    else:
        if "user" in session:
            print('이전에 로그인 했음!!')
            return redirect(url_for("home"))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
                                   
    return redirect(url_for('login'))

if __name__=='__main__':
    init_db()   # 시스템 부팅(?)시에 DB 초기화 하기..
    app.run(debug=True)