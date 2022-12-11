__version__ = '0.1.0'

from flask import Flask
from distributed_restaurant.models.Restaurant import Restaurant

app = Flask(__name__)

restaurant = Restaurant()

from distributed_restaurant.routes import blueprints

for (bp, prefix) in blueprints:
    app.register_blueprint(bp, url_prefix=prefix)