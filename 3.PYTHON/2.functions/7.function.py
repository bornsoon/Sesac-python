def print_gugudan(dan=2, max=10):     # dan의 초기값 설정
    print(f'{dan}단')
    for i in range (1, max+1):
        print(f"{dan} x {i} = {i * dan}")

print_gugudan(3, 20)

print_gugudan(max=20, dan=3)

print_gugudan(max=9)
print_gugudan(9)