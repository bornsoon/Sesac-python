users = {}
user_name = input("사용자의 이름을 입력하시오: ")
user_score = float(input("사용자의 점수를 입력하시오: "))
users[user_name] = user_score

user_name2 = input("사용자의 이름을 입력하시오: ")
user_score2 = float(input("사용자의 점수를 입력하시오: "))
users[user_name2] = user_score2

print(users)
print(max(list(users.values())))