from flask import Flask, render_template, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'abcd1234'
app.permanent_session_lifetime = timedelta(minutes=5) # 5분후에 만료 days=7

items = {
    'item1': {'name':'상품1', 'price':1000, 'image': 'item1.jpg'},
    'item2': {'name':'상품2', 'price':2000, 'image': 'item2.jpg'},
    'item3': {'name':'상품3', 'price':3000, 'image': 'item3.jpg'},
}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    print(f'상품담기: {item_name}')
    # t상품을 세션안의 cart라는 변수에 담기
    if 'cart' not in session:
        session['cart'] = {}
        session.permanent = True
    
    # 카트에 물건을 담기
    if item_name in session['cart']:
        session['cart'][item_name] += 1
    else:
        item_info = items.get(item_name)
        if item_info:
            session['cart'][item_name] = 1

    # 세션 정보가 변경된 것을 알려주기
    session.modified = True

    return redirect(url_for('index'))

@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    print(f'상품 지우기: {item_name}')
    # 상품 지우는 코드 작성하기
    if 'cart' in session and item_name in session['cart']:
        session['cart'].pop(item_name)
        session.modified = True

    return redirect(url_for('view_cart'))

@app.route('/clear_cart')
def clear_cart():
    print(f'카트 비우기')
    if 'cart' in session:
        session.pop('cart')
        session.modified = True

    return redirect(url_for('view_cart'))


@app.route('/view_cart')
def view_cart():
    cart_items = {}
    total_price = 0

    for item_name, quantity in session.get('cart', {}).items(): # 세션 안의 cart라는 변수의 dict 객체들 가져오기
        item = items.get(item_name) # 첫번째 항목의 아이템을 DB에서 조회하기
        if item:
            # 프론트에서 표현하기 위한 key, value들 모아서 담기
            cart_items[item_name] = {'name': item['name'], 'quantity': quantity, 'price': item['price'], 'image': item['image']}
            total_price += item['price'] * quantity

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)