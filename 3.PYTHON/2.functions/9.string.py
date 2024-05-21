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
print(s.lower())
print(s.upper())
print(s.islower())
print(s.isupper())
print(l.islower())
print(l.isupper())
print(u.islower())
print(u.isupper())
print(s.capitalize())
print(s.title())