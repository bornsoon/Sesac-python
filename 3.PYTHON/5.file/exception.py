def div(a, b):
    try:
        result = a / b
        print("실제결과는: ",result)
    except Exception as e:
        print("알 수 없는 오류가 발생했습니다. 오류코드: ", e)
        return "Nan"
    
    return result

print(div(5,3))
print(div(10,0))
print(div(15,0))
print(div(15,"a"))