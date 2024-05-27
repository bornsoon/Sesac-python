import random

class GenderGenerator:
    gender = ['Male', 'Female']

    def generate_gender(self):
        return random.choice(self.gender)