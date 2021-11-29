import functools
# will need to import sqlalchemy possibly Marshmallow

from flask import (
        Blueprint, flash, g, redirect, request, session, url_for
        )

from werkzeug.security import check_password_hash, generate_password_hash

from src.db import get_db


bp = Blueprint('api', __name__, url_prefix='/api/v0')

@bp.route('/users', methods('GET', 'POST', 'DELETE', 'PATCH'))

def register():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        db = get_db()
        error = None

    if not first_name:
        error = "First and last name are required"
    elif not last_name:
        error = "First and last name are required"
    
    # if error is None:
    #     try:
    #         db.execute(


    #                 )

    
