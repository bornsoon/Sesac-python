# 이진 탐색 (binary_search)

def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2 # 소숫점을 버리는 나눗셈
        if list[mid] == target:
            return mid # 정답 찾았음
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

my_list = [1, 3, 5, 7 ,9, 11, 13, 15, 17, 19]

target = 19

result = binary_search(my_list, target)
if result != -1:
    print("타겟 인덱스: ", result)
else:
    print("타겟 없음")