from distributed_restaurant import __version__
from distributed_restaurant.models.Order import Order
from distributed_restaurant.models.RestaurantItem import RestaurantItem

from tasks import make_meal


def test_version():
    assert __version__ == '0.1.0'

def test_make_meal():
    order = Order([RestaurantItem(1, 'Pizza Pequena', 34.99, 20),
        RestaurantItem(2, 'Pizza Média', 65.99, 20),
        RestaurantItem(3, 'Pizza Grande', 85.99, 20),
        RestaurantItem(4, 'Batata Frita', 15.99, 3),
        RestaurantItem(5, 'X-Salada', 25.99, 10),
        RestaurantItem(6, 'Cerveja litro', 12.99, 1),
        RestaurantItem(7, 'Temaki', 19.99, 15)], 1, 2)
    print(order)
    result = make_meal.apply_async(order, queue='chef').get(timeout=90)
    print('make_meal finished executing on correct time')
