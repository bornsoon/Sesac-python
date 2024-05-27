import calendar
month_lst = ['January','February','March','April','May','June','July','August','September','October','November','December']

class InputError(Exception):
    pass

def get_cal():
    try:
        year = int(input("연도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
    except ValueError:
        raise InputError(" >> 숫자를 입력하세요.")

    if year < 1:
        raise InputError(" >> 1년 이후의 달력만 조회 가능합니다.")
    if month < 1 or month > 12:
        raise InputError(" >> 월에 1~12 사이의 숫자를 입력하세요.")
    
    return year, month

def get_month_day(year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if year%4==0 and year%100!=0 or year%400==0:
            return 29
        else:
            return 28
    else:
        return 31

def cal_cal(year, month):
    cal_days = (year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400
    for i in range(1, month):
        cal_days += int(get_month_day(year, i))
    cal_days += 1
    find_1day = int(cal_days % 7)    # 1일의 요일 구하기
    print(f'     [ {month_lst[month-1]} {year} ]')
    print("SUN MON TUE WED THU FRI SAT")

    show_cal(find_1day, month, year)
            

def show_cal(day1, month, year):
    print('   '*day1+' '*day1, end="")
    for i in range(get_month_day(year, month)):
        if i < 9:
            print(f' {i+1}  ', end="")
        else:
            print(f'{i+1}  ', end="")

        if (i+1+day1)%7 == 0:
            print()


while(True):
    try:
        year, month = get_cal()
    except InputError as e:
        print(e)
    else:
        cal_cal(year, month)
    print()

print_calendar(year, month)