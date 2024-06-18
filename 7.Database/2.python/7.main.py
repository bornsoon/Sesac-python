import db_crud as db

# 메인 함수
def main():
    # 데이터 생성
    db.create_table()

    # 데이터 삽입
    db.insert_user("Alice", 30)
    db.insert_user("Bob", 25)
    db.insert_user("Charlie", 35)

    # 데이터 조회
    print("--- 데이터 조회 ---")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")

    # 데이터 수정
    db.update_users('Alice', 'age', 32)
    print(" --- 앨리스 나이 변경 이후 --- ")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")

    # 데이터 조회
    db.delete_uer("Bob")

    # 데이터 삭제
    print(" --- 밥 삭제 이후 --- ")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("--- 데이터 조회 끝 ---")
    # 데이터 조회
    return

if __name__=="__main__":
    main()