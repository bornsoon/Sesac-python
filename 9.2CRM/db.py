import sqlite3

DATABASE = './crmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn

def get_query(query, params=None, all=True):
    conn = get_db_connection()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    if all == True:
        result = cur.fetchall()
    else:
        result = cur.fetchone()
    conn.close()
    
    return result

def exectue_query(query, params):
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()