from flask import Flask, jsonify, request
from db_be import get_all
import math

app = Flask(__name__)


def pagings(category, str, page, per_page):
    total_page = math.ceil(len(category) / per_page)
    prePage = True if page < 8 else False
    nextPage = True if page < (total_page - 6) else False

    return {"category": str, "total": total_page, "pre": prePage, "next": nextPage }


@app.route('/')
def home():
    return app.send_static_file('user.html')


@app.route('/user', methods=['GET', 'POST'])
@app.route('/user/<int:page>', methods=['GET', 'POST'])
def user(page=1):
    query = "SELECT id, name, gender, age, birthdate FROM users LIMIT 1"
    user = get_all('user')
    
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
    paging = pagings(user, 'user', page, per_page)
    if page < 1:    #### page가 음수일 때 안넘어옴.....ㅠㅠ
        page = 1
    elif page > paging['total']:
        return app.send_static_file('user.html')

    return jsonify({'values': values}, {'page': page}, {'per_page': per_page}, {'paging': paging}, {'name': name}, {'arg': arg})


@app.route('/userDetail/<id>')
def userDetail(id):
    paging = {'category': "user"}
    query = "SELECT id, name, gender, age, birthdate FROM users LIMIT 1"
    user1 = db.get_query(query)
    keys = user1[0].keys()
    user_query = "SELECT name, gender, age, birthdate, address FROM users WHERE id = ?"
    user = db.get_query(user_query, (id,))
    if user:
        user = user[0]

    order_query = "SELECT o.id, o.orderAt, s.name, o.storeId FROM orders o INNER JOIN stores s ON o.storeId=s.Id WHERE o.userId = ? ORDER BY o.orderAt DESC"
    orders = db.get_query(order_query, (id,))

    store_query = "SELECT s.name, s.id, count(s.id) AS 'count' FROM orders o INNER JOIN stores s ON o.storeId=s.Id WHERE o.userId = ? GROUP BY s.Id ORDER BY count(s.Id) DESC LIMIT 5"
    topStores = db.get_query(store_query, (id,))

    item_query = "SELECT i.item, i.id, count(i.item) AS 'count' FROM orderItems oi INNER JOIN items i ON oi.itemId=i.Id INNER JOIN orders o ON oi.orderId=o.id WHERE o.userId = ? GROUP BY i.Id ORDER BY count(i.id) DESC LIMIT 5"
    topItems = db.get_query(item_query, (id,))

    return render_template('userDetail.html', keys=keys, paging=paging, user=user, orders=orders, topStores=topStores, topItems=topItems)


@app.route('/order', methods=['GET', 'POST'])
@app.route('/order/<int:page>', methods=['GET', 'POST'])
def order(page=1):
    query = "SELECT * FROM orders ORDER BY orderAt DESC LIMIT 1"
    order1 = db.get_query(query)
    keys = order1[0].keys()
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
        arg = request.form['arg']
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))
        arg = request.args.get('arg')

    if arg:
        query = "SELECT * FROM orders WHERE orderAt LIKE ?||'%' ORDER BY orderAt DESC"
        order = db.get_query(query, (arg,))
    else:
        query = "SELECT * FROM orders ORDER BY orderAt DESC"
        order = db.get_query(query)

    firstIndex = (page - 1) * per_page
    values = order[firstIndex : firstIndex + per_page]
    paging = pagings(order, 'order', page, per_page)
    if page < 1:    #### page가 음수일 때 안넘어옴.....ㅠㅠ
        page = 1
    elif page > paging['total']:
        return redirect(url_for('user'))

    return render_template('order.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, arg=arg)


@app.route('/orderDetail/<id>')
def orderDetail(id):
    paging = {'category': "order"}
    query = "SELECT * FROM orders LIMIT 1"
    order1 = db.get_query(query)
    keys = order1[0].keys()
    order_query = "SELECT * FROM orders WHERE Id = ?"
    value = db.get_query(order_query, (id,))
    if value:
        value = value[0]

    return render_template('orderDetail.html', paging=paging, value=value, keys=keys)


@app.route('/orderItem', methods=['GET', 'POST'])
@app.route('/orderItem/<int:page>', methods=['GET', 'POST'])
def orderItem(page=1):
    query = "SELECT * FROM orderItems LIMIT 1"
    orderItem1 = db.get_query(query)
    keys = orderItem1[0].keys()
    query = "SELECT * FROM orderItems"
    orderItem = db.get_query(query)
    
    if request.method == 'POST':
        per_page = int(request.form['per_page'])
    elif request.method == "GET":
        per_page = int(request.args.get('per_page', default=20))

    firstIndex = (page - 1) * per_page
    values = orderItem[firstIndex : firstIndex + per_page]
    paging = pagings(orderItem, 'orderItem', page, per_page)
    if page < 1:    #### page가 음수일 때 안넘어옴.....ㅠㅠ
        page = 1
    elif page > paging['total']:
        return redirect(url_for('user'))

    return render_template('orderItem.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging)


@app.route('/orderItemDetail/<id>')
def orderItemDetail(id):
    paging = {'category': "orderItem"}
    query = "SELECT oi.*, i.item, i.price FROM orderitems oi JOIN items i ON oi.ItemId=i.Id WHERE oi.orderId = ?"
    orderItems = db.get_query(query, (id,))
    
    sum_query = "SELECT CAST(SUM(i.price) AS INTEGER) FROM orderitems oi JOIN items i ON oi.ItemId=i.Id WHERE oi.orderId = ? GROUP BY oi.orderId"
    sum = db.get_query(sum_query, (id,))
    if sum:
        sum = f"{sum[0][0]:,}"

    # 인덱스 에러 >> 빈 값 확인하기(SELECT COUNT(*) FROM orders LEFT JOIN orderitems ON orderitems.orderId=orders.Id WHERE orderitems.Id IS NULL;)

    return render_template('orderItemDetail.html', paging=paging, values=orderItems, sum=sum)


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
    if page < 1:    #### page가 음수일 때 안넘어옴.....ㅠㅠ
        page = 1
    elif page > paging['total']:
        return redirect(url_for('user'))

    return render_template('item.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name, arg=arg)


@app.route('/itemDetail/<id>')
def itemDetail(id):
    paging = {'category': "item"}
    query = "SELECT * FROM items LIMIT 1"
    item1 = db.get_query(query)
    keys = item1[0].keys()
    query = "SELECT * FROM items WHERE id = ?"
    item = db.get_query(query, (id,))
    if item:
        item = item[0]

    revenue_query = "SELECT strftime('%Y-%m', OrderAt) AS perMonth, CAST(SUM(price) AS INTEGER), count(oi.Id) FROM orderitems oi INNER JOIN items i ON oi.itemId=i.Id JOIN orders o ON oi.orderId=o.Id WHERE i.id= ? GROUP BY perMonth ORDER BY perMonth DESC"
    revenue = db.get_query(revenue_query, (id,))
    revenues = []
    if revenue:
        for i in revenue:
            revenues.append([i[0], f"{i[1]:,}원", i[2]])

    return render_template('itemDetail.html', keys=keys, paging=paging, item=item, revenues=revenues)


@app.route('/store', methods=['GET', 'POST'])
@app.route('/store/<int:page>', methods=['GET', 'POST'])
def store(page=1):
    query = "SELECT * FROM stores LIMIT 1"
    store1 = db.get_query(query)
    keys = store1[0].keys()
    query = "SELECT * FROM stores"
    store = db.get_query(query)
    
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

    if page < 1:    #### page가 음수일 때 안넘어옴.....ㅠㅠ
        page = 1
    elif page > paging['total']:
        return redirect(url_for('user'))

    return render_template('store.html', keys=keys, values=values, page=page, per_page=per_page, paging=paging, name=name)


@app.route('/storeDetail/<id>')
def storeDetail(id):
    paging = {'category': "store"}
    query = "SELECT * FROM stores LIMIT 1"
    store1 = db.get_query(query)
    keys = store1[0].keys()
    query = "SELECT * FROM stores WHERE id = ?"
    store = db.get_query(query, (id,))
    if store:
        store = store[0]

    revenue_query = "SELECT strftime('%Y-%m', OrderAt) AS perMonth, CAST(SUM(price) AS INTEGER), count(oi.Id) FROM orderitems oi INNER JOIN items i ON oi.itemId=i.Id JOIN orders o ON oi.orderId=o.Id WHERE o.storeID = ? GROUP BY perMonth ORDER BY perMonth DESC"
    revenue = db.get_query(revenue_query, (id,))
    revenues = []
    if revenue:
        for i in revenue:
            revenues.append([i[0], f"{i[1]:,}원", i[2]])

    customer_query = "SELECT o.userId, u.name, count(o.Id) AS Visit FROM orders o INNER JOIN users u ON o.userId=u.Id WHERE o.storeId = ? GROUP BY o.userId ORDER BY Visit DESC LIMIT 10"
    topCustomers = db.get_query(customer_query, (id,))

    return render_template('storeDetail.html', keys=keys, paging=paging, store=store, revenues=revenues, topCustomers=topCustomers)

if __name__ == '__main__':
    app.run(debug=True)