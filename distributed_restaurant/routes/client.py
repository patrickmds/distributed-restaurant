from flask import Blueprint, request, json
from distributed_restaurant import restaurant

bp = Blueprint('client', __name__)

@bp.route('/', methods=['GET'])
def get_clients():
    return json.dumps([obj.__dict__ for obj in restaurant.clients])

@bp.route('/<email>', methods=['GET'])
def get_client(email):
    client = restaurant.get_client(email)
    if not client:
        return 'No client found'
    return json.dumps(client.__dict__)

@bp.route('/', methods=['POST'])
def create_client():
    data = request.json
    if not 'email' in data.keys():
        return 'Missing email field in body'
    client, error = restaurant.register_client(data['email'])
    if (error):
        return error
    return json.dumps(client.__dict__)

@bp.route('/', methods=['DELETE'])
def remove_client():
    data = request.json
    if not 'email' in data.keys():
        return 'Missing email field in body'
    client = restaurant.remove_client(data['email'])
    if not client:
        return 'Client not found'
    return json.dumps(client.__dict__)