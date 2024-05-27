import random
import uuid
import csv
from itertools import chain

class IdGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class NameGenerator:
    names = []

    def __init__(self):
        with open('names.txt', 'r') as file:
            # names = file.read().splitlines()    # 줄단위로 읽기
            csvreader = csv.reader(file)
            csv_list_names = [n for n in csvreader]
            names_list = list(chain(*csv_list_names))
            self.names = [n.strip() for n in names_list]

    def generate_name(self):
        return random.choice(self.names)

class AddressGenerator:
    cities = []

    def __init__(self):
        with open('cities.txt', 'r') as file:
            csvreader = csv.reader(file)
            csv_list_cities = [a for a in csvreader]
            cities_list = list(chain(*csv_list_cities))
            self.cities = [a.strip() for a in cities_list]
    
    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"

class BirthdateGenerator:
    year_start = 1980
    year_end = 2005

    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"         # 한 자릿수를 두 자릿수로 맞추기

class GenderGenerator:
    gender = ['Male', 'Female']

    def generate_gender(self):
        return random.choice(self.gender)

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
            #a_user = (id, name, birthdate, gender, address)
            #data.apend(a_user)

# 메인 함수
if __name__ == "__main__":

    users1 = DataGenerator(5)
    users1.generate_users()     # 실행할 때마다 새로 생성

    for d in users1.data:
        print(d)