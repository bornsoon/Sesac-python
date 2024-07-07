import sqlite3

DATABASE = './crmdb.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn

def get_query(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    result = cur.fetchall()
    result = [dict(row) for row in result]
    
    conn.close()
    return result


def get_query_one(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    result = cur.fetchone()
    result = dict(result)
    
    conn.close()
    return result

def exectue_query(query, params):
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def get_all(category):
    value = get_query("SELECT * FROM ?", (category,))
    values = [dict(row) for row in value]

    return values

