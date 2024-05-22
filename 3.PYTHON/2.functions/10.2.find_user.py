users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
    {"name": "Dave", "age": 35, "location": "Jeju", "car": "BMW"},
    {"name": "June", "age": 35, "location": "Daegu", "car": "Audi"}
]

def find_user2(search):
    result = []

    if search.get('name') is None:     # <-- search['name'] : name값이 없을 때는 가져올 수 없어서 Error
        search['name'] = True
    elif search.get('location') is None:
        search['location'] = True
    elif search.get('age') is None:
        search['age'] = True
    elif search.get('car') is None:
        search['car'] = True

    for u in users:
        if u['name'] == search['name'] and u['age'] == search['age'] and u['location'] == search['location'] and u['car'] == search['car']:
            result.append(u)

    return result

#search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice","age": 40}
# search_criteria3 = {"location": "Jeju", "car": "BMW"}

# print(find_user2(search_criteria1))
print(find_user2(search_criteria2))
# print(find_user2(search_criteria3))