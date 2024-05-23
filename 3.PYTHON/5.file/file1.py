# 파일 입출력을 할 때 사용하는 함수.. open
# 파일 시스템(FAT, FAT32, NTFS, EXT3, EXT4...)

# 파일
# Character Meaning
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' create a new file and open if for writing
# 'a' open for wtriting, appending to the end of the file if it exits
# 'b' binary mode

# file = open('example.txt', 'w')
# with open("example.txt", 'w') as file:
#     file.write('Hello, World\n')

# print('텍스트 파일 기록을 완료하였습니다')
# with open('example.txt', 'r') as file:
#     context = file.read()    # 변수에 파일이 담기므로 메모리 차지
#     print(context)

with open('example.txt', 'r') as file: # 파일에 접근하기 위한 포인터 (파일 디스크립터)
    for line in file:               # 메모리에 파일 용량만큼 공간을 차지하지 않음
        print(line, end='')

with open('example.txt', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')