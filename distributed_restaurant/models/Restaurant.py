from distributed_restaurant.models.Client import Client

class Restaurant:
    
    def __init__(self, name, menu, clients=[], orders=[]):
        self.name = name
        self.menu = menu
        self.clients = clients
        self.orders = orders

    #TODO implement something to consume order, suggestion: something with celery to fullfill teacher requirement

    def register_client(self, email):
        if next((x for x in self.clients if x.email == email), None):
            return None, 'Email already exists'
        client = Client(email)
        self.clients.append(client)
        return client, None

    def register_order(self, order):
        self.orders.append(order)
        return 'Order registered'

    def remove_client(self, email):
        result = next((index for index, obj in enumerate(self.clients) if obj.email == email), None)
        if not result:
            return None
        return self.clients.pop(result)

    def get_client(self, email):
        return next((x for x in self.clients if x.email == email), None)