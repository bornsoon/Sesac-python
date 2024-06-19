from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'hello1234'

# flask_sqlalchemy 설정 끝
db = SQLAlchemy(app)

# 모델 불러오기
# from models import User 
# DB 모델 정의
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(00))
    age = db.Column(db.Integer)
                 

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')

    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update_user():
    id = request.form.get('id')
    name = request.form.get('name')
    age = request.form.get('age')
    user = User.query.filter_by(id=id).first()
    print(user)
    if name:
        user.name = name
        flash('이름 수정 성공!')
        db.session.commit()

    if age:
        user.age = age
        flash('나이 수정 성공!')
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)