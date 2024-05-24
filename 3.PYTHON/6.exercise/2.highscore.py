def select_mode():
    users = {}
    user_name = input("사용자의 이름을 입력하시오: ")

    try:
        user_score = float(input("사용자의 점수를 입력하시오: "))
        users[user_name] = user_score
    except ValueError:
        print("숫자를 입력하세요.")

    while True:
        mode = input("score, high, history 중 원하는 모드를 입력하시오: ")

        if mode == "score":
            user_name = input("사용자의 이름을 입력하시오: ")
            try:
                user_score = float(input("사용자의 점수를 입력하시오: "))
                users[user_name] = user_score
            except ValueError:
                print("숫자를 입력하세요.")
            
            N# print(users)

        elif mode == "high":
            print(max(list(users.values())))

        elif mode == "history":
            for i in users.keys():
                print(" [ 사용자 이름:", i,"/ 점수:",users[i],"]")

        else:
            print("모드 입력이 유효하지 않습니다.")

        y_n = input("계속하시려면 'Y'를, 종료를 원하시면 'N'를 입력하시오; ")
        
        if y_n == "N":
            break

    
select_mode()