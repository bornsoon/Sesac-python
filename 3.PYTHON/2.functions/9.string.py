s = 'Hello World sesac!'
l = 'hello'
u = 'HELLO'
print(s)
print(len(s))
# len()함수는 빌트인 함수!!!
# 모듈---- 객체와 그 객체 안의 함수가 존재함

print(type(s))
# print(lower(s)) XX
# lower(), upper()는 빌트인 함수가 아니라 객체 함수!!!

print()
print(s.lower())  # <---많이 사용됨
print(s.upper())
print(s.islower())  # <---많이 사용됨
print(s.isupper())
print(l.islower())
print(l.isupper())
print(u.islower())
print(u.isupper())
print(s.capitalize())  # <---쓸때없음
print(s.title())  # <---쓸때없음

s2 = ' hello world   !! '
print(s2.strip())  # <---많이 사용됨 (단, 앞뒤의 공백만 제거함)
s3 = 'apple, banana, cherry, orange'
print(s3.split())  # <---많이 사용됨 (기본값은 스페이스)
print(s3.split(','))

s3_list = s3.split(',')
print(s3_list)
s3_clean_list = []
for fruit in s3_list:
    clean_name = fruit.strip()
    s3_clean_list.append(clean_name)
    #s3_clean_list.append(fruit.strip())

print(s3_clean_list)

def parse_input(input):
    s3_clean_list = []
    for fruit in s3_list:
        clean_name = fruit.strip()
        s3_clean_list.append(clean_name)

    return s3_clean_list

s4_list = parse_input(s3)

# 엄~~청나게 좋은건데... 익숙해질 때까지는 시간이 걸림
# list comprehension (리스트 컴프리헨션) = 파이썬의 특징이자 장점

print()
s4_list = [fruit.strip() for fruit in s3.split(',')]
print(s4_list)