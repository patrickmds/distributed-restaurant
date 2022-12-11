
class Order(dict):
    def __init__(self, items, quantity, client_id):
        dict.__init__(
            self, item=[x.to_dict() for x in items],
            quantity=quantity, client_id=client_id
        )
        # self.items = items
        # self.quantity = quantity
        # self.client_id = client_id

    # def __dict__(self):
    #     return {
    #         'items': {x.to_dict() for x in self.items},
    #         'quantity': self.quantity,
    #         'client_id': self.client_id
    #     }
    
    # def __str__(self):
    #     return [str(item) for item in self.items]