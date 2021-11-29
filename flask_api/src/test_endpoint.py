import functools
# will need to import sqlalchemy possibly Marshmallow
from flask import ma

from flask import (
        Blueprint, flash, g, redirect, request, session, url_for, jsonify
        )

# from werkzeug.security import check_password_hash, generate_password_hash

from src.db import get_db


bp = Blueprint('api', __name__, url_prefix='/')

@bp.route('/test', methods=('GET', 'POST', 'DELETE', 'PATCH'))

def test_response():
    print('*************', request, '*************')
    result = {"hello": "world"}
    return jsonify(result)
    # if request.method == "GET":
    #     return "This is an examplt"
        # first_name = request.form['first_name']
        # last_name = request.form['last_name']
        # dob = request.form['dob']
        # db = get_db()
        # error = None

    # if not first_name:
        # error = "First and last name are required"
    # elif not last_name:
        # error = "First and last name are required"
    
    # if error is None:
    #     try:
    #         db.execute(


    #                 )

