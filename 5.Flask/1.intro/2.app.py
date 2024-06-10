from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/user/<name>')  # 기본값의 string으로 처리함
def user(name):
    return f"<H1>Hello, {name}님!<H1>"

@app.route('/user/<int:age>')
def userage(age):
    return f"<h1>Age: {age}</H>"

@app.route('/user/<float:weight>')
def userweight(weight):
    return f"<h1>Weight: {weight}</H>"

@app.route('/user/<name>/<int:age>')
def usernameage(name,age):
    return f"<h1>Hello, {name}님, Age는 {age}입니다.</H>"

@app.route('/user/<name>/<int:age>/weight')
def usernameageweight(name,age,weight):
    return f"<h1>Hello, {name}님, Age는 {age}, Weight는 {weight}입니다.</H>"

if __name__=="__main__":
    app.run(debug=True)