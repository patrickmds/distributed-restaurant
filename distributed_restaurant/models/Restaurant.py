from distributed_restaurant.models.Client import Client
from tasks import make_meal, deliver_meal

class Restaurant:
    
    def __init__(self, name, menu, clients=[], orders=[]):
        self.name = name
        self.menu = menu
        self.clients = clients
        self.orders = orders

    #TODO implement something to consume order, suggestion: something with celery to fullfill teacher requirement

    #--------------- client methods ---------------#
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


    #------------- restaurant methods -------------#
    def get_orders(self):
        return [str(order) for order in self.orders]
    
    def get_orders_by_client_id(self, client_id):
        return [str(order) for order in self.orders if order.client_id == client_id]
    
    def get_menu(self):
        return [item.to_dict() for item in self.menu]

    def create_order(self, order, client_id):
        make_meal.apply_async((order), queue='chef')

        deliver_meal.apply_async((client_id), queue='delivery')
        pass