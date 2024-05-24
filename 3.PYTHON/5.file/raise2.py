class CustomError(Exception):    # Exception 클래스 상속(inheritance)
    # 속성
    # 메소드
    pass

def check_value(value):
    if value < 0 or value >= 100:
        raise CustomError("입력값은 0보다 작거나 100보다 클 수 없습니다.")
    return value

result = check_value(50)     # 대문자로 쓰는 것을 constant로 활용함. 예) PI
result = check_value(20)     # 하지만 파이썬은 상수 constant가 없음
print(result)


result = None

try:                              # try 구문은 짧을 수록 좋다
    result = check_value(100)     # except 구문도 필요한 것으로 최소화 한다.
except CustomError as e:
    print(e)

print(result)