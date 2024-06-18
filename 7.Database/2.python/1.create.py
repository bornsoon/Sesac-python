import sqlite3

# DB에 연력하기
conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기
cur = conn.cursor()

# 커서를 통해서 명령어 보내기  # IF NOT EXIST 없으면 db 만들어졌으면 실행안됨
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (     
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT not NULL,
            age INTEGER NOT NULL)
''')

# 커밋
conn.commit()

# 연결 닫기
conn.close()