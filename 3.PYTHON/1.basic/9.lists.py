# list comprehension 리스트 컴프리헨션
# []
# [표현식 for 항목 in 반복 (조건문)]

# 1. 1부터 9까지의 숫자를 닫는 리스트를 생성하시오
nums = [num for num in range(1, 10)]
    # 최종표현할 변수명(num) for 항목(array(변수명과 같게)) in 반복(range(1,10))

print(nums)

# 2. 위 리스트의 각 숫자의 제곱을 구하고 싶으면??
# [1,2,3,4,...,9]
# [1,4,9,16,...,81]
squares = [x ** 2 for x in range(1, 10)]
print(squares)

# 3. 1부터 20까지의 짝수드로 이루어진 리스트??
even_numbers = [x for x in range(1, 20 + 1) if x % 2 ==0]
odd_numbers = [x for x in range(1, 20 + 1) if x % 2 ==1]
even_numbers1 = [x for x in range(2, 21, 2)]
print(even_numbers)
print(odd_numbers)
print(even_numbers1)

# 4. 문자열의 각 글자를 대문자로 바꾼 리스트를 생성하시오
word = 'hello'
# 원하는 결과1 = ['h', 'e', 'l', 'l', 'o']
# 원하는 결과2 = ['H', 'E', 'L', 'L', 'O']
upper_letter = [char.upper() for char in word]
upper_letter_join = ''.join([char.upper() for char in word])

lower_letter = [char.lower() for char in word]
lower_letter_join = ''.join([char.lower() for char in word])

print(upper_letter)
print(upper_letter_join)
print(lower_letter)