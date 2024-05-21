def hello():
    print('hello1')
    print('hello2')
    print('hello3')

hello()

def numbers(num1):
    result = num1 + 4
    if result > 10:
        return result  # None을 리턴하는 건 파이썬의 특징
                       # Null과 None은 파이썬에서 다름.

num1 = numbers(13)
num2 = numbers(4)

print(num1)
print(num1, num2)

#--------------------------------------

# 미션1. 덧셈을 하는 함수를 작성하시오.
#    숫자 두개를 입력 받아서, 해당 숫자의 합산을 반납한다.

def add(sum1,sum2):
    sum = sum1 + sum2
    return sum

print(add(2,5))
print(add(10,20))

# 파이썬은 return값이 복수개인 특이한 언어
# return값은 변경 불가한 튜플로 반환
def add2(num1,num2):
    return num1, num2, num1 + num2

print(add2(1,2))

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

print(sub(5,3))
print(mul(2,3))
print(div(5,0)) # ZeroDivisionError