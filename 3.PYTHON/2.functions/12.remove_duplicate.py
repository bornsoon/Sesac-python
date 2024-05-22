def remove_duplicate1(lst):
    newLst = []
    duplicate_check = False

    for n in lst:
        duplicate_check = False

        for u in newLst:
            print(f"입력값:{n}, 유닉목록:{u}")

            if n == u:
                print(f"중복: {n} == {u}")
                duplicate_check = True
                break

        if not duplicate_check:
            print(f"중복아닌것:{n}")
            newLst.append(n)
            
    return newLst

# 조금 더 파이썬스러운 스타일

def remove_duplicate2(numbers):
    unique_list = []

    for n in numbers:
        if n in unique_list:
            pass
        else:
            unique_list.append(n)

    return unique_list

# 조금 더더더 파이썬스러운 스타일

def remove_duplicate3(numbers):
    unique_list = []

    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)

    return unique_list

# 모던 파이썬 코드
def remove_duplicate4(numbers):
    return list(set(numbers))

numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
unique_numbers = remove_duplicate1(numbers)
unique_numbers = remove_duplicate2(numbers)
unique_numbers = remove_duplicate3(numbers)
unique_numbers = remove_duplicate4(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)