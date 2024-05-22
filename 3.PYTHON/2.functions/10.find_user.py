users = [  # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
    {"name": "Dave", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "June", "age": 35, "location": "Daegu", "car": "Audi"}
]

# user1{name} == XXX 할 수 없음
# user1['name'] == 가장 일반적인 방식
# user1.get('name') == 함수를 통해서 가져오는 방식
# user1.name == 객체의 멤버를 가져오는 방식

# ... is None

def display_user(users):
    print("--- 찾은 사용자 목록 ---")
    if len(users) == 0:
        print("사용자 없음")
    else:
        for u in users:
            print(f"이름: {u['name']}, 나이: {u['age']}, 사는 곳: {u['location']}")

def find_user(name = None, age= None):
    if type(name) == "int":
        age = name

    found_user = []
    if name is None and age is None:
        return users

    for u in users:
        if name is not None and age is not None:
            if u["name"].lower() == name.lower() and \
               u["age"] == age:
                found_user.append(u)

        elif name is not None:
            if u["name"].lower() == name.lower():
                found_user.append(u)
            
        elif age is not None:
            if u["age"] == age:
                found_user.append(u)

    return found_user
            
found1 = find_user('Alice', 25)
found2 = find_user('alice')
found3 = find_user()
found4 = find_user(25)
display_user(found1)
display_user(found2)
display_user(found3)
display_user(found4)