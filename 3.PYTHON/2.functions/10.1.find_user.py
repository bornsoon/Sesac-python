users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
    {"name": "Dave", "age": 35, "location": "Jeju", "car": "BMW"},
    {"name": "June", "age": 35, "location": "Seoul", "car": "Audi"}
]

def find_user2(search):
    result = []

    for u in users:
        if (search.get('age') is None or u.get('age') == search.get('age')) and \
           (search.get('min_age') is None or u['age'] >= search.get('min_age')) and \
           (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):
            
            result.append(u)

    return result



search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice","age": 40}
search_criteria3 = {"location": "Jeju", "car": "BMW"}
search_criteria4 = {"car": "Audi","age": 40}
search_criteria5 = {"car": "Audi","age": 35}
search_criteria6 = {"name": "Alice","min_age": 30}

print(find_user2(search_criteria1))
print(find_user2(search_criteria2))
print(find_user2(search_criteria3))
print(find_user2(search_criteria4))
print(find_user2(search_criteria5))
print(find_user2(search_criteria6))

def find_user3(search):
    result = []

    for u in users:
        if match_creteria(u, search):
            result.append(u)

    return result

def match_creteria(user, criteria):      # 이 user라는 사용자가 이 조건(criteria)에 만족하느냐??
    for key, value in criteria.items():  # 딕셔너리 안에 있는 key, value 쌍을 하나씩 추출하는 함수
        if key == "age":
            if user["age"] != value:
                return False
        if key == "name":
            if user["name"] != value:
                return False
        if key == "location":
            if user["location"] != value:
                return False
        if key == "car":
            if user["car"] != value:
                return False
            
    return True

print("------")
print(find_user3(search_criteria1))
print(find_user3(search_criteria2))
print(find_user3(search_criteria3))
print(find_user3(search_criteria4))
print(find_user3(search_criteria5))
print(find_user3(search_criteria6))
