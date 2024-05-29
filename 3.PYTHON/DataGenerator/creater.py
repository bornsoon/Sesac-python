import random
import uuid
from csv_operator import  CsvOperator
import sys

csv_operator = CsvOperator()

firstname = csv_operator.read_csv('firstname.csv')
lastname = csv_operator.read_csv('lastname.csv')
city = csv_operator.read_csv('city.csv')
street = csv_operator.read_csv('street.csv')
storetype = csv_operator.read_csv('storetype.csv')
coffee = csv_operator.read_dict('coffee.csv')
beverage = csv_operator.read_dict('beverage.csv')
food = csv_operator.read_dict('food.csv')

class Creater:
    lst = []
    mode = input('원하는 생성모드(user/store/item/order): ')

    def creater(self):
        if self.mode == 'user':
            return self.create_users()
        elif self.mode == 'store':
            return self.create_stores()
        elif self.mode == 'item':
            return self.create_items()
        elif self.mode == 'order':
            return self.create_orders()


    def create_users(self):
        num = int(input('생성하고 싶은 사용자 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'Name', 'Gender', 'Age', 'Birthdate', 'Address'))

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

            self.lst.append((id, name, gender, age, birthdate, address))

        return self.lst


    def create_stores(self):
        num = int(input('생성하고 싶은 점포 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'Name', 'Type', 'Address'))

        for _ in range(num):
            id = str(uuid.uuid4())
            street1 = random.choice(street)
            type = random.choice(storetype)
            name = type + ' '+ street1 + str(random.randint(1,10)) + '호점'
            address = random.choice(city) + '시 ' + street1 + ' ' + str(random.randint(1,99)) + '길 ' + str(random.randint(1,99))

            self.lst.append((id, name, type, address))

        return self.lst
    

    def create_items(self):
        num = int(input('생성하고 싶은 아이템 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'Item', 'Type', 'Price'))

        for _ in range(num):
            id = str(uuid.uuid4())
            type = random.randint(1,3)

            if type == 1:
                type = 'coffee'
                item = random.choice(coffee)
            elif type == 2:
                type = 'beverage'
                item = random.choice(beverage)
            else:
                type = 'food'
                item = random.choice(food)
            
            self.lst.append((id, item['menu'], type, item['price']+'원'))

        return self.lst


    def create_orders(self, users, stores):
        num = int(input('생성하고 싶은 주문 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'OrderAt', 'StoreID', 'UserID'))

        for _ in range(num):
            id = str(uuid.uuid4())
            date = f'{random.randint(2014, 2024)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}'
            time = f'{random.randint(1,24):02d}-{random.randint(1,60):02d}-{random.randint(1,60):02d}'
            storeID = random.choice(stores[0])
            userID = random.choice(users[0])

            self.lst.append((id, date + ' '+ time, storeID, userID))

        return self.lst


class Creater1(Creater):
    printmode= input('원하는 출력모드(csv/screen): ')
    lst = []
    lst = Creater()
    lst = lst.creater()
    

    def creater_print(self):
        if self.printmode == 'csv':
            filename = input('파일 이름: ') + '.csv'
            csv_operator.print_csv(self.lst, filename)
        elif self.printmode == 'screen':
            csv_operator.print_screen(self.lst)
        else:
            print('유효하지 않는 입력값입니다')



if __name__ == "__main__":
    create1 = Creater1()
    create1.creater_print()