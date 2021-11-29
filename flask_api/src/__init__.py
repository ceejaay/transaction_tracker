import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    db = SQLAlchemy(app)
    api = Api(app)
    ma = Marshmallow(app)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # @app.route('/hello')
    # def hello():
    #     return "hello world"

    from . import db
    db.init_app(app)

    from . import test_endpoint
    app.register_blueprint(test_endpoint.bp)
    app.add_url_rule('/test', endpoint="users")

    # from . import api_guts
    # app.register_blueprint(bp)
    # app.add_url_rule('/merchants', endpoint="users")
    print("*****************", app, "***************")


    return app

