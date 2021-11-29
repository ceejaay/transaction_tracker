from flask import Blueprint, request, g, session, url_for
from flask_api import db
from flask_api.test.models import Test
test_endpoint = Blueprint('test', __name__, url_prefix='/test')

@test_endpoint.route('/endpoint', methods=["GET"])
def hello():
    return "hello wordl"



