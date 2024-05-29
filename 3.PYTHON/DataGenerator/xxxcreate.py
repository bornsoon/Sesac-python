import random
import uuid
from csv_operator import  CsvOperator

csv_operator = CsvOperator()

firstname = csv_operator.read_csv('firstname.txt')
lastname = csv_operator.read_csv('lastname.txt')
city = csv_operator.read_csv('city.txt')
street = csv_operator.read_csv('street.txt')
storetype = csv_operator.read_csv('storetype.txt')

def create_users():
    num = int(input('생성하고 싶은 사용자 갯수: '))
    users = []
    users.append(('id', 'name', 'gender', 'age', 'birthdate', 'address'))

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
        users.append(_user)

    return users

def create_stores():
    num = int(input('생성하고 싶은 점포 갯수: '))
    stores = []
    stores.append(('id', 'name', 'address'))

    for _ in range(num):
        id = str(uuid.uuid4())
        street1 = random.choice(street)
        name = street1 + str(random.randint(1,10)) + '호점'
        address = random.choice(city) + '시 ' + street1 + ' ' + str(random.randint(1,99)) + '길 ' + str(random.randint(1,99))

        _stores = ( id, name, address )
        stores.append(_stores)

    return stores

users = create_users()
csv_operator.print_csv(users, 'users.txt')
csv_operator.print_screen(users)

stores = create_stores()
csv_operator.print_csv(stores, 'stores.txt')
csv_operator.print_screen(stores)