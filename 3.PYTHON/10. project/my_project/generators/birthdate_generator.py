import random

class BirthdateGenerator:
    year_start = 1980
    year_end = 2005

    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"         # 한 자릿수를 두 자릿수로 맞추기