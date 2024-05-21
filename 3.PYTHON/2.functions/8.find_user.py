users = [  # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
]

# users = ["Alice", "Bob", "Charlie"]  # 스트링 리스트

# user1{name} == XXX 할 수 없음
# user1['name'] == 가장 일반적인 방식
# user1.get('name') == 함수를 통해서 가져오는 방식
# user1.name == 객체의 멤버를 가져오는 방식

#name = input("찾는 사용자의 이름을 입력하시오.: ")

def find_user(name):
    found_user = []
    for u in users:
        #print(u['name'])
        if u['name'].lower() == name.lower():
            # print(u)
            found_user.append(u)
    return found_user
        #print("찾는 사용자가 없습니다.")
            

found = find_user('tony')
print(f"찾은 사용자: {found}")