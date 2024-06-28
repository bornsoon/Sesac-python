from flask import Flask, render_template, redirect, request, url_for
import db as db
import math

app = Flask(__name__)


def pagings(category, page, per_page):
    total_page = math.ceil(len(category) / per_page)
    prePage = True if page < 8 else False
    nextPage = True if page < (total_page - 6) else False

    return {"category": 'user', "total": total_page, "pre": prePage, "next": nextPage }


@app.route('/')
def home():
    return redirect(url_for('user'))


@app.route('/user', methods=['GET', 'POST'])
@app.route('/user/<int:page>', methods=['GET', 'POST'])
def user(page=1):
    query= "SELECT id, name, gender, age, birthdate FROM users LIMIT 1"
    user1 = db.get_query(query)
    keys = user1[0].keys()

    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        name = request.form['name']
        gender = request.form['gender']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        name = request.args.get('name')
        gender = request.args.get('gender')

    if gender:
        query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%' AND gender = ?"
        params = (name, gender)
    else:
        if not name:
            name = ""
        query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%'"
        params = (name, )

    user = db.get_query(query, params)

    firstIndex = (page - 1) * per_page
    values = user[firstIndex : firstIndex+per_page]
    
    paging = pagings(user, page, per_page)

    return render_template('user.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name, gender=gender)


@app.route('/order')
def order():
    query= "SELECT id, name, gender, age, birthdate FROM order"
    data = db.get_query(query)
    keys = data[0].keys()
    

    return render_template('table.html', keys=keys, values=values, page=page, paging=paging, name=name, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)