def input_age(age):
    if age < 0:       # if문으로 예외처리하는 것도 실무에서 많이 씀
        # print("음수를 넣을 수 없습니다.")
        # retun None
        raise ValueError("음수를 입력할 수 없습니다.")
        
    print(age)

    return age

try:
    input_age(10)
    input_age(15)
    input_age(-2)
except ValueError as e:
    print("입력값에 오류가 있습니다.")