from flask import (
        Blueprint, flash, g, redirect, request, url_for
        )

from werkeuf.exceptions import abort

from src.db import get_db

bp = Blueprint('api_guts', __name__)

@bp.route('/merchants')
def merchants():
    db = get_db()
    
