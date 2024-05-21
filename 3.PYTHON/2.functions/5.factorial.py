num = int(input("원하는 숫자를 입력하시오.: "))

def factorial(num):
    fac = 1
    for i in range(1, num+1):
        fac *= i
    print("{}의 팩토리얼은 {}입니다.".format(num,fac))

factorial(num)