from flask import Flask, jsonify, request
from models import Transactions, User, Merchant
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

class MerchantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Merchant


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "dob")


class TransactionSchema(ma.Schema):
    class Meta:
        fields = (
                "id",
                "description",
                "amount",
                "credit",
                "debit",
                "user_id",
                "merchant_id",
                )

