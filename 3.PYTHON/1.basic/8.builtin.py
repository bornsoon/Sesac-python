# while True: #조건문이 '참'인동안 실행한다.
#    a = input("숫자를 입력하세요: ")
#    print(a)

str_a = input("첫 번째 숫자를 입력하세요: ")
str_b = input("두 번째 숫자를 입력하세요: ")

# input 값의 모든 것은 다 문자열로 처리한다.
# type casting = 타입 변환

int_a = int(str_a)
int_b = int(str_b)

print(f"두 숫자의 합은 {int_a + int_b}입니다.")