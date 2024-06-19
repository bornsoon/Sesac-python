from app import db

# DB 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(00))
    age = db.Column(db.Integer)
