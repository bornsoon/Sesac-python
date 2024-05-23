contents = ""

try:
    with open("file.txt", "r", encoding='utf-8') as file:
        contents = file.read()
        file.write('Hello')
except:
    print('알 수 없는 오류가 발생했습니다.')
# except FileNotFoundError:
#     print("파일이 없습니다.")
# except PermissionError:
#     print("해당 파일에는 쓰기 권한이 없습니다.")
# except IOError:
#     print("해당 파일에 내용을 읽고/쓰고 할 수 없습니다.")

print("파일내용:", contents)