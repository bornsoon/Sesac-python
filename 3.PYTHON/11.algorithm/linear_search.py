import random
import time
# 선형 탐색 (Linear Search)

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return -1

def generate_random_numbers(count):
    random_numbers = [random.randint(1, count) for _ in range(count)]
    return random_numbers

my_list = generate_random_numbers(5_000)
target = 7

start_time = time.time()
result = linear_search(my_list, target)
end_time = time.time()

diff_time = end_time - start_time
print(f"찾는데 걸린 시간은: {diff_time} seconds")

if result != -1:
    print("타겟을 찾았습니다: index", result)
else:
    print("타겟이 존재하지 않습니다")