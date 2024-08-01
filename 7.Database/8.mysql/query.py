import pymysql

host = '192.168.56.101'
user = 'sesac'
password = 'sesac1234'
database = 'sesac'

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM user")
results = cursor.fetchall()

for res in results:
    print(res)


# 1. 패키지 설치한다.  apt install xxxx
# 2. 설정파일 변경한다.  /etc/xxxx
# 3. 데몬 재시작한다.  systemctl restart xxxx