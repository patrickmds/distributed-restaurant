import uuid

class Client:

    def __init__(self, email):
        self.email = email
        self.id = uuid.uuid4().hex