interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data.sort())  # sort()는 None 값 리턴!
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)