from flask_sqlalchemy import SQLAlchemy

# Flask - SQLAlchemy를 연결할건데... 일단 app을 못가져오니
#           일단 비워둠....
db = SQLAlchemy()

# 클래스를 통해서 DB 테이블을 설계/설정할 수 있음...
class User(db.Model):
    __tablename__ = 'users'  # 옵셔널 한것... 테이블명이 클래스명과 다를 때 설정함...
    id = db.Column(db.Integer, primary_key=True)  # PRIMARY KEY
    name = db.Column(db.String, nullable=False) # VARCHAR(20), NOT NULL
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):  # 나의 객체를 누군가 print할 때, 표현해주고 싶은 함수를 구현하면 됨...
        return f'<사용자: {self.id}, {self.name}, {self.age}>'