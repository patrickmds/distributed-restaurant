import json

from flask import Blueprint
from distributed_restaurant import app
from distributed_restaurant.routes.client import bp as client_bp

bp = Blueprint('index', __name__)

@bp.route("/")
def index():
    return "<p> Health Check </p>"

blueprints = [
    (bp, '/'),
    (client_bp, '/client')
]