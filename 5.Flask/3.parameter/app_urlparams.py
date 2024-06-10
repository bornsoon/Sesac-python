from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-555'}
]

@app.route('/')
def home():
    return jsonify(users)  # JSON 포맷으로 변환하는 함수

@app.route('/user/<name>')
def search_user(name):
    user = None
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
            break
        if str(u['age']) == name:   #curl -i 127.0.0.1:5000/user/30 나이로 찾기
            user = u
            break

    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'user not found'}), 404

if __name__=="__main__":
    app.run(debug=True)