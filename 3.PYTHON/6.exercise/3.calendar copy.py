import calendar

year = int(input("연도를 입력하시오: "))
month = int(input("월을 입력하시오: "))

def print_calendar(year, month):
    if year <= 0 or month not in range(1,13):
        raise ValueError ("입력값에 오류가 있습니다.")
    
    # year년 1월 1일의 요일, () 은 1년 1월부터 입력달까지 윤년이 존재했던 횟수
    DDD = (year + ( (year - 1) // 4 - (year -1) // 100 + (year - 1) // 400))  % 7 - 1

    if month == 1:                                 # 평년일 때의 각 달의 요일
        MDDD = DDD
        print(f"     January  {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 2:
        MDDD = (DDD + 3) % 7
        print(f"     Febuary  {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 28 + 1
    elif month == 3:
        MDDD = (DDD + 2) % 7 + 1
        print(f"      March   {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 4:
        MDDD = (DDD + 5) % 7 + 1
        print(f"      April   {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 30 + 1
    elif month == 5:
        MDDD = DDD % 7 + 1
        print(f"       May    {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 6:
        MDDD = (DDD + 3) % 7 + 1
        print(f"      June    {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 30 + 1
    elif month == 7:
        MDDD = (DDD + 5) % 7 + 1
        print(f"      July    {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 8:
        MDDD = (DDD + 1) % 7 + 1
        print(f"     August   {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 9:
        MDDD = (DDD + 4) % 7 + 1
        print(f"    September {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 30 + 1
    elif month == 10:
        MDDD = (DDD - 1) % 7 + 1
        print(f"     October  {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1
    elif month == 11:
        MDDD = (DDD + 2) % 7 + 1
        print(f"    November  {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 30 + 1
    elif month == 12:
        MDDD = (DDD + 4) % 7 + 1
        print(f"    December  {year}")
        print(f"Mo Tu We Th Fr Sa Su")
        lastday = 31 + 1

    # 윤년 체크
    yun = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0)
    if yun == 1 and month != 1 and month != 2:
        MDDD = MDDD % 7 + 1
    if yun == 1 and month == 2:
        lastday += 1

    print("   " * (MDDD - 1), end = "")

    for i in range(1,lastday):
        if i <10:
            print(f" {i} ", end = "")
        else:
            print(f"{i} ", end = "")
        if (i + MDDD - 1) % 7 == 0:
        # if (i + MDDD - 1) % 7 == 0:
            print("")

# print("   라이브러리\n", calendar.month(year, month))     # 비교 체크
try:
    print_calendar(year, month)
except ValueError as e:
    print("입력값에 오류가 있습니다.")