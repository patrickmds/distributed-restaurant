
class Order:
    def __init__(self, items, quantity, client_id):
        self.items = items
        self.quantity = quantity
        self.client_id = client_id
    
    def __str__(self):
        return [str(item) for item in self.items]