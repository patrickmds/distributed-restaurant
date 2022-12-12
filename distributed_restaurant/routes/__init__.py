import json

from flask import Blueprint
from distributed_restaurant import app
from distributed_restaurant.routes.order import bp as order_bp
from distributed_restaurant.routes.client import bp as client_bp
from distributed_restaurant.routes.restaurant import bp as restaurant_bp

bp = Blueprint('index', __name__)

@bp.route("/")
def index():
    return "<p> Health Check </p>"

blueprints = [
    (bp, '/'),
    (order_bp, '/order'), 
    (client_bp, '/client'), 
    (restaurant_bp, '/restaurant')
]