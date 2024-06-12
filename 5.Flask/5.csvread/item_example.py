my_dict = {'name':'Alice', 'age':25, 'phone':'123-456-7890'}
# print(my_dict['age'])

# built-in 함수 = 내장함수
items = my_dict.items()
items_list = list(items)    # type casting = 형변환
# print(items_list[0])
print(type(items_list[0])) 

for item in items_list:
    print(item)

for key, value in items_list:
    print(f'키: {key}, 값: {value}')
    

print('-'* 50)

for key, value in items_list:
    print(f'키: {key}, 값: {value}')

for key, value in sorted(my_dict.items()):
    print(f'키: {key}, 값: {value}')

my_dict['phone'] = '123-555-7890'

print(my_dict)

update_dict = {'car': 'K5', 'city': 'Seoul'}

# for key, value in update_dict.items():
#     my_dict[key] = value

print(f'원본: {my_dict}')
print(f'업데이트: {update_dict}')

new_dict = my_dict | update_dict  # python 3.9 이상~
print(f'통합본: {new_dict}')

print('-'* 50)

users = [
    {'name':'Alice', 'age':25, 'phone':'123-456-7890'},
    {'name':'Bob', 'age':19, 'phone':'123-222-7890'},
    {'name':'NewBob', 'phone':'123-222-7890'},
    {'name':'Charlie', 'age':22, 'phone':'123-333-7890'}
]

filtered_user = []

# for user in users:
#     if user['age'] >= 20:
#         filtered_user.append(user)    # NewBob에 age가 없기 때문에 crush

for user in users:
    if user.get('age', 0) >= 20:      # get() 함수 -> 키가 존재하지 않으면 0으로 기본값 설정
        filtered_user.append(user)

filtered_user1 = [user for user in users if user.get('age', 0) >= 20]
print(filtered_user1)

filtered_user_age = [{key: value for key, value in u.items() if key == 'age' and \
                      value >= 20} for u in users]
print(filtered_user_age)