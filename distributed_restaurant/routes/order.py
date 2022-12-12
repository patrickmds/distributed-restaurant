from flask import Blueprint, request, json
from distributed_restaurant import restaurant
from distributed_restaurant.models.Order import Order
from distributed_restaurant.models.OrderState import OrderState

bp = Blueprint('order', __name__)

@bp.route('/', methods=['GET'])
def get_orders():
    return json.dumps(restaurant.get_orders())


@bp.route('/<client_id>', methods=['GET'])
def get_orders_by_client_id(client_id):
    return restaurant.get_orders_by_client_id(client_id)

@bp.route('/', methods=['POST'])
def create_order():
    data = request.json
    if not 'email' in data.keys():
        return 'Missing email field in body'
    if not 'items' in data.keys():
        return 'Missing items field in body'
    if not 'money' in data.keys():
        return 'Missing money field in body'
    email = data['email']
    items = data['items']
    money = data['money']

    client = restaurant.get_client((email))
    if not client:
        return 'Client not registered yet. please register'
    if len(items) < 2:
        return 'Your Order must have at least one item'
    value = restaurant.get_order_value(items)
    change = money - value
    if change < 0:
        return 'I thinks you miscalculated the order price, please gives us the right amount of money'
    restaurant.pay(value)

    order = Order(items, OrderState.WAITING, client.id)
    restaurant.create_order(order, client.id)

    toReturnOrder.order = order.id
    toReturnOrder.change = change
    return json.dumps(toReturnOrder)

@bp.route('/<order_id>', methods=['POST'])
def confirm_order_delivered(order_id):
    if not order_id:
        return 'What will you confirm if no id is given? Please insert valid order_id to confirm order delivered'
    order = restaurant.get_order(order_id)
    if not order:
        return 'Are you sure you ordered with us, we did not find this order_id among our orders'
    restaurant.confirm_order_delivered(order_id)
    return json.dumps(order)