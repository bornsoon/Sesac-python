import sqlite3

# 사용자 DB
DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 행을 sqlite3.Row라는 객체 타입으로 반환
                                    #이걸 설정하면 각 Row의 결과는 Dict유형으로 반환됨.
    return conn

def get_query(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result

def execute_query(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT)
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                title TEXT,
                content TEXT,
                FOREIGN KEY (id) REFERENCES users(id))
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