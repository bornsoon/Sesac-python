import random              # import, from 순.. 기능별/알파벳 순으로 정렬
import uuid
from csv_operator import  CsvOperator

csv_operator = CsvOperator()

# import할 때 다 실행되어버림 >> 함수로 통째로 따로 분리 or 클래스 생성자 초기화!!!! (init) csv_input csv_temp csv_output
firstname = csv_operator.read_csv('./csvs/firstname.csv')
lastname = csv_operator.read_csv('./csvs/lastname.csv')
city = csv_operator.read_csv('./csvs/city.csv')
street = csv_operator.read_csv('./csvs/street.csv')
storetype = csv_operator.read_csv('./csvs/storetype.csv')
coffee = csv_operator.read_dict('./csvs/coffee.csv')
beverage = csv_operator.read_dict('./csvs/beverage.csv')
food = csv_operator.read_dict('./csvs/food.csv')


class Generator:
    lst = []

    def generator(self):
        mode = input('원하는 생성모드(user/store/item/order/orderItem): ')
        if self.mode.lower() == 'user':
            return self.generate_users()
        elif self.mode.lower() == 'store':
            return self.generate_stores()
        elif self.mode.lower() == 'item':
            return self.generate_items()
        elif self.mode.lower() == 'order':
            return self.generate_orders()
        elif self.mode.lower() == 'orderitem':
            return self.generate_orderItems()
        else:
            print('생성모드에서 유효하지 않은 값이 입력되었습니다.')
            raise ValueError


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
            age = 2024 - year         # 2024 << THIS_YEAR 상수 처리하고 위에 빼놓기
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
        
        try:
            users = input('가져올 user 파일명: ')
            users = csv_operator.read_dict(users)
            stores = input('가져올 store 파일명: ')
            stores = csv_operator.read_dict(stores)
        except Exception as e:
            print("파일명이 유효하지 않습니다.")
            exit()

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
        
        try:
            orders = input('가져올 order 파일명: ')
            orders = csv_operator.read_dict(orders)
            items = input('가져올 item 파일명: ')
            items = csv_operator.read_dict(items)
        except Exception as e:
            print("파일명이 유효하지 않습니다.")
            exit()

        for _ in range(num):
            id = str(uuid.uuid4())
            orderId = random.choice(orders)['Id']
            itemId = random.choice(items)['Id']

            self.lst.append((id, orderId, itemId))

        return self.lst