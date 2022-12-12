from flask import Blueprint, request, json
from distributed_restaurant import restaurant

bp = Blueprint('restaurant', __name__)

@bp.route('/menu', methods=['GET'])
def get_menu():
    return json.dumps(restaurant.get_menu())

