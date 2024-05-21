# 1. 일반 문자열 출력
print('-1-')
print('hello')
print('hello world')
print('hello','world')
print(1,2,3)

# 2. f-문자열 (f-string) 사용한 출력
print('-2-')
print(f"hello {1}")
내변수='123'
print(f"hello {내변수}")
my_variable='456'
print(f"helo {내변수} 는 {my_variable}")

# 3. 문자열 포맷팅 {} 를 사용한 치환
print('-3-')
name="홍길동"
print("Hello, {}".format(name))
print("Hello, {} x {} = {}".format(내변수, my_variable, name))

# 4. 문자열 포맷팅에 순번 부여하기 {0}
print('-4-')
print("Hello, {0} x {1} = {2}".format(내변수, my_variable, name))
print("Hello, {2} x {0} = {1}".format(내변수, my_variable, name))
print("Hello, {2} x {1} = {0}".format(내변수, my_variable, name))

# 5. 문자열 연결 연산자
print('-5-')
print('hello', end="\t")
print('world', end="")      #줄바꿈하기 싫을 때!!!
print('sesac')

# 6. % 연산자
print('-6-')
age = 30
print('Hello, %s' %name)    # %s 는 문자열(string)
print('Hello, %d' %age)     # %d 는 숫자(decimal)
print('Hello, %s' %age)
# print('Hello, %d' %name)  TypeError: %d format: a real number is required, not str