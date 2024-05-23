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

numbers = [1, 2, 3, 4, 5]

def random_list(elements):
    random.shuffle(elements)
    return elements

print("원본 리스트1:",elements)
print("원본 리스트2:",numbers)
print("섞인 리스트:",random_list(elements))
print("섞인 리스트:",random_list(numbers))



# 5. 랜덤으로 문자열 생성 (영문 대문자 6자리)
strU = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def random_Upper():
    random_Upper=[]
    for i in range(6):
        random_Upper.append(strU[random.randint(0, len(strU)-1)])
    return random_Upper

#print(strU[len(strU)-1])
print("5. 랜덤 대문자 6자리:",''.join(random_Upper()))
    


# 6. 랜덤 초이스에서 가중치를 고려한 랜덤
class NotSameNumError(Exception):
    def __init__(self):
        super().__init__("원하는 랜덤 숫자의 갯수와 가중치의 갯수가 일치하지 않습니다")

def weighed_random_element():
    elements2 = []
    # try:
    #     wantPer.append(int(input("원하는 숫자의 가중치(정수)를 위의 입력의 순서에 맞춰 입력하시오: ").split(',')))
        
    #     if len(elements) != len(wantPer):
    #         raise NotSameNumError
        
    # except TypeError:
    #     return "입력값에 숫자가 아닌 값이 왔습니다."
    # except Exception as e:
    #     print("예외가 발생했습니다.", e)

    wantPer = input("원하는 숫자의 가중치(정수)를 위의 입력의 순서에 맞춰 입력하시오: ").split(',')

    for i in range(len(wantPer)):
        for j in range(int(wantPer[i])):
            elements2.append(elements[i])
    
    # print(wantPer)
    # print(elements2)

    return random.choice(elements2)

print("6. 당첨된 과일은:", weighed_random_element())

    

# 7. 랜덤 비밀번호 생성 (대소문자, 숫자 포함 8자리)
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
strL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
str = []
str=[strL, strU, num]
str = [x for y in str for x in y]
def random_pw():
    random_pw=[]
    for i in range(8):
        random_pw.append(str[random.randint(0, len(str)-1)])
    return random_pw

print("7. 랜덤 비밀번호 8자리:", ''.join(random_pw()))


# 8. 랜덤 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리)
def random_pw2():
    str2 = [random.choice(strL), random.choice(strU), random.choice(num)]
    str2.append(random_pw())
    str2 = [x for y in str2 for x in y]
    random.shuffle(str2)
    return str2

print("8. 강력한 랜덤 비밀번호 8자리:", ''.join(random_pw2()))