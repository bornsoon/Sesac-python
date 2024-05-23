def div(a, b):
    try:
        result = a / b
        print("실제결과는: ",result)
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "입력값에 숫자가 아닌 값이 왔습니다."
    except:
        print("알 수 없는 이유로 나눌 수 없습니다.")
        return "NaN"
    else:
        print("오류가 안나고 계산을 잘 완료했습니다.")
    finally:
        print("여기는 오류/성공 무조건 호출됩니다")
    
    return result

print(div(5,3))
print(div(10,0))
print(div(15,0))
print(div(15,"a"))

# 문자형 -> 정수형으로 변환
def convert_to_interger(num_str):
    try:
        result = int(num_str)
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        return None

    return result

print(convert_to_interger("20"))
print(convert_to_interger("a"))