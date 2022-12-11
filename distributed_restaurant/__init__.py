__version__ = '0.1.0'

from flask import Flask
from distributed_restaurant.models.Restaurant import Restaurant
from distributed_restaurant.models.Client import Client
from distributed_restaurant.models.Order import Order
from distributed_restaurant.models.RestaurantItem import RestaurantItem

app = Flask(__name__)

# restaurant = Restaurant()

# preloading configs, used for test purposes
menu = [RestaurantItem(1, 'Pizza Pequena', 34.99, 20),
        RestaurantItem(2, 'Pizza Média', 65.99, 20),
        RestaurantItem(3, 'Pizza Grande', 85.99, 20),
        RestaurantItem(4, 'Batata Frita', 15.99, 3),
        RestaurantItem(5, 'X-Salada', 25.99, 10),
        RestaurantItem(6, 'Cerveja litro', 12.99, 1),
        RestaurantItem(7, 'Temaki', 19.99, 15)]
restaurant = Restaurant('Testes Bar & Lanches', menu)

from distributed_restaurant.routes import blueprints

for (bp, prefix) in blueprints:
    app.register_blueprint(bp, url_prefix=prefix)