from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = './newcrmdb.db'

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM stores")
    stores = cur.fetchall()
    conn.close()
    
    return render_template('index.html', stores=stores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # 외부의 접속을 허용