# print('*')
# print('**')
# print('***')
# print('****')

row = int(input('출력을 원하는 높이를 입력하세요: '))
for i in range(1,row + 1):
    print('*' * i)

# row = input('출력을 원하는 높이를 입력하세요: ')
# num_rows = int(row)
# for i in range(1,num_rows + 1):
#     print('*' * i)

#      *
#     **
#    ***
#   ****
#  *****
print()

for i in range(1, row + 1):
    print(' ' * (row-i) + '*' * i)  # 공백도 출력해야 함!

print()

for i in range(1, row + 1):
    print(' ' * (row-i) + '*' * (2 * i - 1))

for i in range(1, row):
    print(' ' * i + '*' * (2 * (row-i) -1))

for i in range(row-1, 0, -1):   
    # row-1, row-2, ... , 1 ***0까지가 아니라 1까지임의 주의!!!
    print(' ' * (row-i) + '*' * (2 * i - 1))