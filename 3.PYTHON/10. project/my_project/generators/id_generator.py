import uuid

class IdGenerator:
    def generate_id(self):
        return str(uuid.uuid4())