from generators.address_generator import AddressGenerator
from generators.birthdate_generator import BirthdateGenerator
from generators.gender_generator import GenderGenerator
from generators.id_generator import IdGenerator
from generators.names_generator import NameGenerator     # __pycache__는 빠른 실행을 위해서 클래스를 미리 컴파일 해놓은 파일
from printers.output_printer import DataPrinter
import sys                                               # 시스템으로부터 사용자 입출력을 받음

class DataGenerator:
    data = []
    numbers = 1

    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birthdate_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_users(self):
        self.data = []                           # 함수 실행을 반복할 때마다 초기화하기 위해서 (이 줄을 빼면 리스트에 추가됨)
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birthdate_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()

            self.data.append((id, name, birthdate, gender, address))  # append()는 인자가 하나여야 함... 튜플로 한번에 넣기
            # a_user = (id, name, birthdate, gender, address)
            # self.data.apend(a_user)


# 메인 함수
if __name__ == "__main__":
    my_printer = DataPrinter()

    if len(sys.argv) <= 1:  #사용자 입력 인자가 없으면..
        num_data = input("생성을 원하는 데이터 개수를 입력하세요: ")
    else:                   # 사용자 입력 인자가 있으면...
        num_data = sys.argv[1]
        
    users1 = DataGenerator(int(num_data))
    users1.generate_users()     # 실행할 때마다 새로 생성
        
    my_printer.print_to_screen(users1.data)


    # argv[0] = 실행파일명, arvc[1] = 실제 첫번째 인자값
    # print("입력 인자 확인: 첫 번째 인자: {}, 두 번째 인자: {}".format(sys.argv[0],sys.argv[1])

    # num_data = input('생성을 원하는 데이터 개수를 입력하세요: ')

    # 우리가 원하는 데이터 출력 - 화면, 파일
    if len(sys.argv) == 3:
        if sys.argv[2] == 'screen':
            my_printer.print_to_screen(users1.data)
        elif sys.argv[2] == 'file':
            my_printer.print_to_file(users1.data)
        else:
            print("지원되지 않는 인자")
