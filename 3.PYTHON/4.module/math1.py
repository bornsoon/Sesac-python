import math # 함수는 바로 사용 가능
# import numpy (설치 필요)

# from math import pi, sqrt  
        # pi  / sqrt(4.0) 처럼 바로 쓸 수 있음
# import math as m
        # m.pi  / m.sqrt(4.0)
# import math import pi as p, sqrt as s
        # p / s(4.0)
# del math  >> 가져온 묘듈 해제

# 모듈명.함수명 / 모듈명.상수명
# 상수와 함수는 바로 호출이 가능함

print(math.pi)
print(math.pow(5, 2)) # 5의 2승 = 25

# 원의 넓이 : pi * r ^ 2
radius = 5
area = math.pi * math.pow(radius, 2)
print(f'반지름이 {radius} 인 원의 넓이는 {area} 입니다.')

# 로그 계산
x = 2.718
log_value = math.log(x)
print("natural log: ", log_value)

# 0.0 부터 5.0까지 0.1씩 증가
# for i in numpy.arange(0, 5, 0.1):
#     print(i)