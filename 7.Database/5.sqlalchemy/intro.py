# ORM = SQL을 몰라도, 그냥 나의 개발언어를 통해서 개발을 하겠다.
# Object Relational Model = DB에 들어가는 Table을 Object로 만들어둔 것
# 파이썬에서의 Object란?? Class임....

# 파이썬에서 대표적인 라이브러리 sqlalchemy    >> JAVA는 JPA
# 플라스크에서 더 편하게 만들어둔 것이 flask_sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')  # sqlite를 통해서 사용
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute(query, params)
    # conn.commit()
    # conn.close()

# 테이블의 원형(기본형)
Base = declarative_base()

# 테이블을 설계한다 (이때, 이 테이블이 가져야 하는 기본 속성을 원형으로부터 상속받는다)
class User(Base):
    __tablename__ = 'users'  # 안할경우에는, 이 클래스명 = 테이블명
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# CREATE TABLE users (
#    id INTEGER PRIMARY KEY NOT NULL,
#    name STRING,
#    age INTEGER
#    )

# 설계한 내용을 실행한다.
Base.metadata.create_all(engine)

# 이렇게 만들어진 DB와 통신을 통해서.. 데이터 입출력을 하는 걸... 세션이라고 부르기로 했음...

Session = sessionmaker(bind=engine)
session = Session()

# 이 session을 통해서 자유롭게 CRUD가 가능해지는 것...

new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

new_user = User(name="Bob", age=25)
session.add(new_user)
session.commit()

# INTEGER INTO users (name, age) VALUES ('Alice', 30);

# 사용자 조회하기
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# 10줄짜리 코드를 3줄로 짠것임...
# conn = get_db_connection()
# cur = conn.cursor()
# query = "SELECT * FROM users;"
# result = cur.execute(query, params)
# conn.commit()
# conn.close
# for result in results