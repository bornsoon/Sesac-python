from generator import Generator
from csv_operator import  CsvOperator

csv_operator = CsvOperator()

class Generator1(Generator):     # 불필요한 함수 제거하기 , 내가 원하는 시점에 내가 해당하는 함수를 불러서 실행하기
    
    def generator_print(self):
        printmode= input('원하는 출력모드(csv/screen): ') # input 위치 주의
        lst = []
        try:
            lst = Generator().generator()
        except ValueError as e:
            exit()

        if self.printmode.lower() == 'csv':
            filename = input('파일 이름: ') + '.csv'
            csv_operator.print_csv(lst, filename)
        elif self.printmode.lower() == 'screen':
            csv_operator.print_screen(lst)
        else:
            raise ValueError



if __name__ == "__main__":     # 이 파일 내에서만 실행됨!
    try:
        generate1 = Generator1()
        generate1.generator_print()
    except ValueError as e:
        exit()