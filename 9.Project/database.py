import sqlite3

DATABASE = './newcrmdb.db'

def get_stores():
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute("SELECT * FROM stores")
    stores = cur.fetchall()
    stores = [dict(row) for row in stores]
    conn.close()

    return stores


def get_store_by_name(name):
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute("SELECT * FROM stores WHERE Name Like ?", ('%' + name + '%',))
    stores = cur.fetchall()
    stores = [dict(row) for row in stores]
    conn.close()

    return stores