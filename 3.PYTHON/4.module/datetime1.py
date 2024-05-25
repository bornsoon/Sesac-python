# https://docs.python.org/ko/3/library/datetime.html
import datetime # 객체라서 호출해야 사용가능
import time

# 모듈명.(클래스)객체명.함수명 (Class/Object)

# 현재 시간 출력
now = datetime.datetime.now()
print(now)

# 내가 원하는 시간 생성
my_time = datetime.datetime(2024, 1, 1, 10, 30, 0)
print(my_time)
print(type(my_time))

# delta 함수로 전날 출력하기
print("365일전:",now -datetime.timedelta(1)*365)
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now -delta
    print(date)

ret=datetime.datetime.strptime("2020-05-04","%Y-%m-%d")
print(ret,type(ret))

while True:
    print(now)
    time.sleep(1)