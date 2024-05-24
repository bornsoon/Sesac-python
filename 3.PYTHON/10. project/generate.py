import random

surname = ['김', '박', '이']
middlename = ['수', '민', '태', '여']
lastname = ['원', '림', '미']

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    return name

for _ in range(11):
    print(generate_name())