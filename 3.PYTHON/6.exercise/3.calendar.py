import calendar

# print(calendar.month(2024, 5))

year = int(input("연도를 입력하시오: "))
month = int(input("월을 입력하시오: "))

print(calendar.month(year, month))

def print_calendar(year, month):
    print(f"      Jan  {year}")
    print(f"Mo Tu We Th Fr Sa Su")
    for i in range(1,32):
        if i <10:
            print(f" {i} ", end="")
        else:
            print(f"{i} ", end="")
        if i % 7 ==0:     # 7의 배수네?? 그럼 줄바꾸자
            print("")

print_calendar(2024, 5)