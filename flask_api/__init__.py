from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

from flask_api.test.controllers import test_endpoint as test_module
app.register_blueprint(test_module)


db.create_all()
