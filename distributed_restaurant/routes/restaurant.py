from flask import Blueprint, request, json
from distributed_restaurant import restaurant

bp = Blueprint('restaurant', __name__)

@bp.route('/', methods=['GET'])
def get_orders():
    return json.dumps(restaurant.get_orders())

@bp.route('/menu', methods=['GET'])
def get_menu():
    return json.dumps(restaurant.get_menu())

@bp.route('/<order_id>', methods=['GET'])
def get_orders_by_client_id(client_id):
    return restaurant.get_orders_by_client_id(client_id)
