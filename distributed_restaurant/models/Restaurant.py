import time 

from distributed_restaurant.models.OrderState import OrderState
from distributed_restaurant.models.Client import Client
from tasks import deliver_meal
from threading import Lock

class Restaurant:
    
    def __init__(self, name, menu, clients=[], orders=[], profit = 0):
        self.name = name
        self.menu = menu
        self.clients = clients
        self.orders = orders
        self.profit = profit
        self.mutex = Lock()

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
    
    def get_order_value(self, items):
        price = 0
        for item in items:
            in_menu = next((x for x in self.menu if x.item_id == item['id']), None)
            if in_menu:
                price += in_menu.price* item['quantity']
        return price

    def get_preparation_time(self, order):
        time = 0
        for item in order.items:
            in_menu = next((x for x in self.menu if x.item_id == item['id']), None)
            if in_menu:
                time += in_menu.preparation_time
        if not time:
            time = 10
        return time
    
    def get_orders_by_client_id(self, client_id):
        return [str(order) for order in self.orders if order.client_id == client_id]
    
    def get_menu(self):
        return [item.to_dict() for item in self.menu]

    def create_order(self, order, client_id):
        order.state = OrderState.COOKING
        self.prepare_order(order)
        order.state = OrderState.DELIVERING
        preparation_time = self.get_preparation_time(order)
        deliver_meal.apply_async(args=(preparation_time,), queue='deliver_meal')

    def get_order(self, order_id):
        return next((x for x in self.orders if x.id == order_id), None)
        
    def prepare_order(self, order):
        time_ = self.get_preparation_time(order)
        time.sleep(time_)

    def confirm_order_delivered(self, order_id):
        result = next((index for index, obj in enumerate(self.orders) if obj.id == order_id), None)
        if not result:
            return None
        return self.orders.pop(result)

    def pay(self, payment):
        try:
            self.mutex.acquire()
            self.profit += payment
        finally:
            self.mutex.release()
