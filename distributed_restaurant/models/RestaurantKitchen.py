import time

class RestaurantKitchen:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    """ This method abstracts the preparation of food in the kitchen
        The inputs from restaurant.orders come from the Restaurant class and
        run only handles them by waiting X seconds before defining them as
        complete
    """
    def run(self):
        while True:
            if not self.restaurant.orders:
                time.sleep(5)
            
            order = self.restaurant.orders.pop(0)
            for item in self.order.items:
                # TODO: add this to celery dedicated task queue instead

                time.sleep(item.preparation_time)
            
            yield order
