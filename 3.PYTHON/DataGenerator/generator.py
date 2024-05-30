import random
import uuid
from csv_operator import  CsvOperator

csv_operator = CsvOperator()

firstname = csv_operator.read_csv('./csvfiles/firstname.csv')
lastname = csv_operator.read_csv('./csvfiles/lastname.csv')
city = csv_operator.read_csv('./csvfiles/city.csv')
street = csv_operator.read_csv('./csvfiles/street.csv')
storetype = csv_operator.read_csv('./csvfiles/storetype.csv')
coffee = csv_operator.read_dict('./csvfiles/coffee.csv')
beverage = csv_operator.read_dict('./csvfiles/beverage.csv')
food = csv_operator.read_dict('./csvfiles/food.csv')


class Generator:
    lst = []
    mode = input('원하는 생성모드(user/store/item/order/orderItem): ')

    def generator(self):
        if self.mode == 'user':
            return self.generate_users()
        elif self.mode == 'store':
            return self.generate_stores()
        elif self.mode == 'item':
            return self.generate_items()
        elif self.mode == 'order':
            return self.generate_orders()
        elif self.mode == 'orderItem':
            return self.generate_orderItems()
        else:
            print('유효하지 않는 입력값입니다.')
            exit()


    def generate_users(self):
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


    def generate_stores(self):
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
    

    def generate_items(self):
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


    def generate_orders(self):
        num = int(input('생성하고 싶은 주문 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'OrderAt', 'StoreId', 'UserId'))
        users = input('가져올 user 파일명: ')
        users = csv_operator.read_dict(users)
        stores = input('가져올 store 파일명: ')
        stores = csv_operator.read_dict(stores)

        for _ in range(num):
            id = str(uuid.uuid4())
            date = f'{random.randint(2014, 2024)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}'
            time = f'{random.randint(0,23):02d}-{random.randint(0,59):02d}-{random.randint(1,59):02d}'
            storeId = random.choice(stores)['Id']
            userId = random.choice(users)['Id']

            self.lst.append((id, date + ' '+ time, storeId, userId))

        return self.lst
    

    def generate_orderItems(self):
        num = int(input('생성하고 싶은 주문아이템 갯수: '))
        self.lst = []
        self.lst.append(('Id', 'OrderId', 'ItemId'))
        order = input('가져올 order 파일명: ')
        order = csv_operator.read_dict(order)
        item = input('가져올 item 파일명: ')
        item = csv_operator.read_dict(item)

        for _ in range(num):
            id = str(uuid.uuid4())
            orderId = random.choice(order)['Id']
            itemId = random.choice(item)['Id']

            self.lst.append((id, orderId, itemId))

        return self.lst


class Generator1(Generator):
    printmode= input('원하는 출력모드(csv/screen): ')
    lst = []
    lst = Generator()
    lst = lst.generator()
    

    def generator_print(self):
        if self.printmode == 'csv':
            filename = input('파일 이름: ') + '.csv'
            csv_operator.print_csv(self.lst, filename)
        elif self.printmode == 'screen':
            csv_operator.print_screen(self.lst)
        else:
            print('유효하지 않는 입력값입니다.')



if __name__ == "__main__":
    generate1 = Generator1()
    generate1.generator_print()