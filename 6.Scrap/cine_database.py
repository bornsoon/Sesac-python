import sqlite3

DATABASE = 'movies.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS movies(
                rank TEXT NOT NULL,
                title TEXT NOT NULL,
                audience TEXT NOT NULL,
                link
                )
    ''')
    conn.commit()

    return conn, cur

def save_to_db(conn, cur, params):
    cur.execute('''
        INSERT INTO movies (rank, title, audience, link) VALUES (?,?,?,?)
    ''', (params))
    conn.commit()


def query_movie(cur):
    cur.execute('SELECT rank, title, audience FROM movies')
    rows = cur.fetchall()
    for row in rows:
        print(f'순위: {row[0]}, 영화제목: {row[1]}, 관객수: {row[2]}')

def close_db(conn):
    conn.close()