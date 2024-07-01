from flask import Flask, render_template, redirect, request, url_for
import db as db
import math

app = Flask(__name__)


def pagings(category, str, page, per_page):
    total_page = math.ceil(len(category) / per_page)
    prePage = True if page < 8 else False
    nextPage = True if page < (total_page - 6) else False

    return {"category": str, "total": total_page, "pre": prePage, "next": nextPage }


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
        arg = request.form['arg']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        name = request.args.get('name')
        arg = request.args.get('arg')

    if arg and name:
        query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%' AND gender = ?"
        params = (name.strip(), arg)
    else:
        if arg:
            query = "SELECT id, name, gender, age, birthdate FROM users WHERE gender = ?"
            name = ""
            params = (arg,)
        else:
            if not name:
                name = ""
            query= "SELECT id, name, gender, age, birthdate FROM users WHERE name LIKE ?||'%'"
            arg = ""
            params = (name.strip(),)

    user = db.get_query(query, params)

    firstIndex = (page - 1) * per_page
    values = user[firstIndex : firstIndex + per_page]
    paging = pagings(user, 'user', page, per_page)

    return render_template('user.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name, arg=arg)


@app.route('/userDetail/<id>')
def userDetail(id):
    paging = {'category': "user"}
    user_query= "SELECT name, gender, age, birthdate, address FROM users WHERE id = ?"
    user = db.get_query(user_query, (id,))
    keys = user[0].keys()

    order_query = "SELECT o.id, o.orderAt, s.name, o.storeId FROM orders o INNER JOIN stores s ON o.storeId=s.Id WHERE o.userId = ? ORDER BY o.orderAt DESC"
    orders = db.get_query(order_query, (id,))

    store_query = "SELECT s.name, count(s.id) AS 'count' FROM orders o INNER JOIN stores s ON o.storeId=s.Id WHERE o.userId = ? GROUP BY s.Id ORDER BY count(s.Id) DESC LIMIT 5"
    topStores = db.get_query(store_query, (id,))

    item_query = "SELECT i.item, count(i.item) AS 'count' FROM orderItems oi INNER JOIN items i ON oi.itemId=i.Id INNER JOIN orders o ON oi.orderId=o.id WHERE o.userId = ? GROUP BY i.Id ORDER BY count(i.id) DESC LIMIT 5"
    topItems = db.get_query(item_query, (id,))

    return render_template('userDetail.html', keys=keys, paging=paging, user=user[0], orders=orders, topStores=topStores, topItems=topItems)


@app.route('/order', methods=['GET', 'POST'])
@app.route('/order/<int:page>', methods=['GET', 'POST'])
def order(page=1):
    query= "SELECT * FROM orders ORDER BY orderAt DESC"
    order = db.get_query(query)
    keys = order[0].keys()
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        arg = request.form['arg']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        arg = request.args.get('arg')
    print(arg)

    if arg:
        query = "SELECT * FROM orders WHERE orderAt LIKE ?||'%' ORDER BY orderAt DESC"
        order = db.get_query(query, (arg,))

    firstIndex = (page - 1) * per_page
    values = order[firstIndex : firstIndex + per_page]
    paging = pagings(order, 'order', page, per_page)

    return render_template('order.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, arg=arg)


@app.route('/orderItem', methods=['GET', 'POST'])
@app.route('/orderItem/<int:page>', methods=['GET', 'POST'])
def orderItem(page=1):
    query= "SELECT * FROM orderItems"
    orderItem = db.get_query(query)
    keys = orderItem[0].keys()
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))

    firstIndex = (page - 1) * per_page
    values = orderItem[firstIndex : firstIndex + per_page]
    paging = pagings(orderItem, 'orderItem', page, per_page)

    return render_template('orderItem.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging)


@app.route('/item', methods=['GET', 'POST'])
@app.route('/item/<int:page>', methods=['GET', 'POST'])
def item(page=1):
    query = "SELECT * FROM items ORDER BY type, price LIMIT 1"
    item1 = db.get_query(query)
    keys = item1[0].keys()
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        name = request.form['name']
        arg = request.form['arg']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        name =request.args.get('name')
        arg = request.args.get('arg')

    if arg and name:
        query = "SELECT * FROM items WHERE item LIKE '%'||?||'%' and type = ?"
        params = (name.strip(), arg)
        item = db.get_query(query, params)
    else:
        if arg:
            query = "SELECT * FROM items WHERE type = ?"
            name = ""
            params = (arg,)
        else:
            if not name:
                name =""
            query = "SELECT * FROM items WHERE item LIKE '%'||?||'%'"
            args = ""
            params = (name.strip(),)
        
    item = db.get_query(query, params)

    firstIndex = (page - 1) * per_page
    values = item[firstIndex : firstIndex + per_page]
    paging = pagings(item, 'item', page, per_page)

    return render_template('item.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name, arg=arg)


@app.route('/store', methods=['GET', 'POST'])
@app.route('/store/<int:page>', methods=['GET', 'POST'])
def store(page=1):
    query= "SELECT * FROM stores"
    store = db.get_query(query)
    keys = store[0].keys()
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        name = request.form['name']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        name = request.args.get('name')

    if name:
        query = "SELECT * FROM stores WHERE name LIKE '%'||?||'%'"
        store = db.get_query(query, (name.strip(),))
    else:
        name = ""

    firstIndex = (page - 1) * per_page
    values = store[firstIndex : firstIndex + per_page]
    paging = pagings(store, 'store', page, per_page)

    return render_template('store.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name)


@app.route('/storeDetail/<id>')
def storeDetail(id):
    paging = {'category': "store"}
    store_query= "SELECT * FROM stores WHERE id = ?"
    store = db.get_query(store_query, (id,))
    keys = store[0].keys()

    revenue_query = "SELECT strftime('%Y-%m', OrderAt) AS perMonth, CAST(SUM(price) AS INTEGER), count(oi.Id) FROM orderitems oi INNER JOIN items i ON oi.itemId=i.Id JOIN orders o ON oi.orderId=o.Id WHERE o.storeID = ? GROUP BY perMonth ORDER BY perMonth DESC"
    revenue = db.get_query(revenue_query, (id,))

    customer_query = "SELECT o.userId, u.name, count(o.Id) AS Visit FROM orders o INNER JOIN users u ON o.userId=u.Id WHERE o.storeId = ? GROUP BY o.userId ORDER BY Visit DESC LIMIT 10"
    topCustomers = db.get_query(customer_query, (id,))

    return render_template('storeDetail.html', keys=keys, paging=paging, store=store[0], revenue=revenue, topCustomers=topCustomers)

if __name__ == '__main__':
    app.run(debug=True)