from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # 괄호 안에 200은 기본값

@app.route("/user")
@app.route("/user/<name>")
def user(name=""):
    friends = ['bill', 'steve', 'larry']
    return render_template("user.html", username = name, content = friends)

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__=="__main__":
    app.run(debug=True)