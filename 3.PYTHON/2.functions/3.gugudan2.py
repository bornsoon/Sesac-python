def print_gugudan(dan):
    print(f'{dan}단')
    for i in range (1, 10):
        print(f"{dan} x {i} = {i * dan}")

for i in range(2, 10):
    print_gugudan(i)
    print()

# for dan in range(1,10):
#     print(f'{dan}단')
#     for i in range (1, 10):
#         print(f"{dan} x {i} = {i * dan}")
#         print()