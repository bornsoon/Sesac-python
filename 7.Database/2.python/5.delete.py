import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute('DELETE FROM users WHERE name = ?', ("Bob",))
cur.execute('DELETE FROM users WHERE name = ?', ("Alice",))

conn.commit()
conn.close()