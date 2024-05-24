# 계산기 코드 작성하기
# 1. 연산자 및 두개의 숫자를 입력받아 그 결과를 입력하시오.
# 2. 무한박복하기

# ---사용자 입력값을 받아 계산하기---
# 1. 사용자에게 연산자를 선택하게 한다.
#    (예시에 나오지 않은 연산자를 선택하면 오류를 발생시킨다.)
# 2. 사용자가 계산하고 싶은 피연산자 2개를 하나씩 입력받는다.
#    (숫자값이 아닐 경우는 예외 발생,
#     위에서 나누는 연산을 선택했을 경우 두번째 값이 0일 때도 예외 발생,
#     제곱을 선택했을 경우 연산자는 하나만 선택받아야함 )
# 3. 계산값을 출력해준다.
# 4. 입력값을 초기화해주고 다음 입력을 대기한다.

def calculation(operator, num1, num2):
    if operator == "+":
        return(num1 + num2)
    if operator == "-":
        return(num1 - num2)
    if operator == "*":
        return(num1 * num2)
    if operator == "/":
        return(num1 / num2)
    if operator == "^":
        return(num1 ** 2)
    
def cal():
    operator = input("원하는 계산의 연산자를 선택하시오(덧셈: +, 뺄셈 : -, 곱하기: *, 나누기:/, 제곱: ^): ").strip()

    if operator not in ("+", "-", "*", "/", "*", "^"):
        print("연산자 입력값이 유효하지 않습니다.")
        return None

    try:
        num1 = float(input("첫번째 피연산자 값을 입력하시오: "))

        if operator != "^":
            num2 = float(input("두번째 피연산자 값을 입력하시오: "))

            if num2 == 0:
                print("나누기의 두번째 피연산자값은 0이 아닌 값을 입력하시오: ")
                return None
            else:                 
                print(calculation(operator, num1, num2))
                print("종료를 원하시면 <Ctrl + C> 를 누르시오.")
        
        else:
            print(calculation(operator, num1, num2=1))
            print("종료를 원하시면 <Ctrl + C> 를 누르시오.")
            
    except TypeError:
        return "입력값에 숫자가 아닌 값이 왔습니다."
        

while True:
    cal()