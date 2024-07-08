from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3
import bcrypt

# 사용자 로그인 요약정리
# 1-1. DB초기화 시 사용자ID/hash암호화된 계정 정보로 DB를 생성한다.
# 1-2. 이때 bcrypt함수를 통해 salt를 추가해서 암호를 생성한다.
# 2-1. 로그인 시 사용자가 입력한 값을 bcrypt.checkpw함수를 통해서 DB와 비교한다.
# 2-2. 다양한 문자열들이 입력될 수 있는 것을 고려하여 입력값을 코딩한다.

app = Flask(__name__)
app.secret_key = 'hello1234'

DATABASE = 'users.db'

def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():    # DB 초기화는 수동으로도 많이 함
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # try:
    #     cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', ('username', 'password'))
    # except sqlite3.IntegrityError as e:
    #     print(f"Error creating user 'username': {e}")
    db.commit()
    db.close()


def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, hashed_password))
        db.commit()
        print(f"User {username} created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error creating user {username}: {e}")
    
    cursor.close()
    db.close()


def query_db(query, args=(), isOne=False):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return (result[0] if result else None) if isOne else result


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        user = query_db('SELECT * FROM users WHERE username=?', (username,), isOne=True)

        if user and bcrypt.checkpw(password, user['password']):
            print('사용자 로그인 성공')
            return redirect(url_for('dashboard'))
        else:
            print('사용자 로그인 실패')
            flash('로그인 실패. 사용자 이름 또는 비밀번호가 올바르지 않습니다', 'danger')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    flash('로그인 성공', 'success')
    return render_template('dashboard.html')

if __name__=='__main__':
    # with app.app_context():
    init_database()

    users = [
        {'user1', 'pass1'},
        {'user2', 'pass2'}
    ]

    for username, password in users:
        create_user(username, password)

    app.run(debug=True)