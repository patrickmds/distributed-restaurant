
import uuid

class Order():
    def __init__(self, items, state, client_id):
        self.id = uuid.uuid4().hex
        self.items = items
        self.state = state
        self.client_id = client_id

    # def __dict__(self):
    #     return {
    #         'items': {x.to_dict() for x in self.items},
    #         'quantity': self.quantity,
    #         'client_id': self.client_id
    #     }
    
    # def __str__(self):
    #     return [str(item) for item in self.items]