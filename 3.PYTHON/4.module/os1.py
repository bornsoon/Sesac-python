import os

current_dir = os.getcwd()
print(f"현재 작업 디렉토리: {current_dir} 입니다.")

new_dir = "내폴더123"
os.mkdir(new_dir)
print(f"생선된 디렉토리명은 {new_dir} 입니다.")

os.rmdir(new_dir)
print(f"디렉토리명 ${new_dir} 이 삭제되었습니다.")

my_path = os.getenv("PATH")
print(f"나의 환경변수는 {my_path}")

command = "dir"
os.system(command)

os.chdir("C:/Sesac/sesac")
print(f"현재 작업 디렉토리는 {os.getcwd()}")
os.system(command)