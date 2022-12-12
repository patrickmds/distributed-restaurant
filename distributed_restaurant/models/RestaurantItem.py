
class RestaurantItem:
    def __init__(self, item_id, name, price, preparation_time):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.preparation_time = preparation_time

    def __str__(self):
        return f'Item({self.item_id}, {self.name}, {self.preparation_time})'

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'preparation_time': self.preparation_time
        }