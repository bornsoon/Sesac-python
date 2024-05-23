import random

print(random.randint(1,10))

print((str(6 * random.random()+1)).split(".")[0])

def roll_dice():
    return random.randint(1,6)

print("주사위를 던진 결과는:", roll_dice())

elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
def choose_random_element():
    # return elements[random.randint(0,len(elements)-1)]
    return random.choice(elements)

print("당첨된 과일은:", choose_random_element())

elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
numbers = [1, 2, 3, 4, 5]

def random_list(elements):
    random.shuffle(elements)
    return elements

print("원본 리스트1:",elements)
print("원본 리스트2:",numbers)
print("섞인 리스트:",random_list(elements))
print("섞인 리스트:",random_list(numbers))


# 5. 랜덤으로 문자열 생성 (영문 대문자 6자리)


# 6. 랜덤 초이스에서 가중치를 고려한 랜덤


# 7. 랜덤 비밀번호 생성 (대소문자, 숫자 포함 8자리)


# 8. 랜덤 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리)

