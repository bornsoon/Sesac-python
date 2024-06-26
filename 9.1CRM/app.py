from flask import Flask, render_template
import db as db

app = Flask(__name__)

@app.route('/')
@app.route('/user')
@app.route('/user/<page>')
def user():
    query = "SELECT * FROM users"
    values = db.get_query(query)
    keys = values[0].keys()
    return render_template('user.html', keys=keys, values=values)

if __name__ == '__main__':
    app.run(debug=True)