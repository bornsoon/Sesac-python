import csv
import random
from itertools import chain

class AddressGenerator:
    cities = []

    def __init__(self):
        with open('cities.txt', 'r', encoding = 'utf-8') as file:
            csvreader = csv.reader(file)
            csv_list_cities = [a for a in csvreader]
            cities_list = list(chain(*csv_list_cities))
            self.cities = [a.strip() for a in cities_list]
    
    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"