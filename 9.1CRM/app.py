from flask import Flask, render_template, redirect, request, url_for
import db as db
import math

app = Flask(__name__)

def pagings(category, page):
    total_page = math.ceil(len(category) / 20)
    prePage = True if page < 8 else False
    nextPage = True if page < (total_page - 6) else False

    return {"category": 'user', "total": total_page, "pre": prePage, "next": nextPage }


@app.route('/')
def home():
    return redirect(url_for('user'))


@app.route('/user')
@app.route('/user/<int:page>')
def user(page=1):
    name = request.form.get('name')
    gender = request.form.get('gender')
    
    query = "SELECT id, name, gender, age, birthdate FROM users"

    if name or gender:
        query= "SELECT * FROM users WHERE name LIKE '%name%'"

    user = db.get_query(query)
    keys = user[0].keys()
    firstIndex = (page - 1) * 20
    values = user[firstIndex : firstIndex+20]
    
    paging = pagings(user, page)

    return render_template('user.html', keys=keys, values=values, page=page, paging=paging)


if __name__ == '__main__':
    app.run(debug=True)