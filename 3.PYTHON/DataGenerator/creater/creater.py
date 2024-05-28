import random
import uuid
from csv_operator import  CsvOperator

csv_operator = CsvOperator()

firstname = csv_operator.read_csv('firstname.txt')
lastname = csv_operator.read_csv('lastname.txt')
city = csv_operator.read_csv('city.txt')
street = csv_operator.read_csv('street.txt')
storetype = csv_operator.read_csv('storetype.txt')

class Creater:
    lst = []
    mode = input('원하는 생성모드(users/stores): ')

    def creater(self):
        if self.mode == 'users':
            return self.create_users()
        elif self.mode == 'stores':
            return self.create_stores()

    def create_users(self):
        num = int(input('생성하고 싶은 사용자 갯수: '))
        self.lst = []
        self.lst.append(('id', 'name', 'gender', 'age', 'birthdate', 'address'))

        for _ in range(num):
            id = str(uuid.uuid4())
            name = random.choice(firstname) + random.choice(lastname)
            year = random.randint(1950, 2010)
            month = random.randint(1,12)
            day = random.randint(1,28)
            birthdate = f'{year}-{month:02d}-{day:02d}'
            age = 2024 - year
            gender = random.choice(['Male', 'Female'])
            address = random.choice(city) + '시 ' + random.choice(street) + ' ' + str(random.randint(1,99)) + '길 ' + str(random.randint(1,99))

            _user = ( id, name, gender, age, birthdate, address )
            self.lst.append(_user)

        return self.lst

    def create_stores(self):
        num = int(input('생성하고 싶은 점포 갯수: '))
        self.lst = []
        self.lst.append(('id', 'name', 'type', 'address'))

        for _ in range(num):
            id = str(uuid.uuid4())
            street1 = random.choice(street)
            type = random.choice(storetype)
            name = type + ' '+ street1 + str(random.randint(1,10)) + '호점'
            address = random.choice(city) + '시 ' + street1 + ' ' + str(random.randint(1,99)) + '길 ' + str(random.randint(1,99))

            _stores = ( id, name, type, address )
            self.lst.append(_stores)

        return self.lst


class Creater1(Creater):
    printmode= input('원하는 출력모드(csv/screen): ')
    lst = []
    filename = input('파일 이름: ') + '.txt'
    lst = Creater()
    lst = lst.creater()

    def creater_print(self):
        if self.printmode == 'csv':
            csv_operator.print_csv(self.lst, self.filename)
        elif self.printmode == 'screen':
            csv_operator.print_screen(self.lst)

create1 = Creater1()
create1.creater_print()