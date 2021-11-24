from flask import Flask, jsonify, request
from models import Transactions, User, Merchant
from schema import MerchantSchema, UserSchema, TransactionSchema
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


merchant_schema = MerchantSchema()
merchants_schema = MerchantSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

# resources


class MerchantListResource(Resource):
    def get(self):
        merchants = Merchant.query.all()
        return merchants_schema.dump(merchants)

    def post(self):
        new_merchant = Merchant(
                name=request.json['name'],
                description = request.json['description'],
                timestamp  = datetime.now()
        )
        db.session.add(new_merchant)
        db.session.commit()
        return merchant_schema.dump(new_merchant)

api.add_resource(MerchantListResource, '/merchants/')

class MerchantResource(Resource):

    def get(self, merchant_id):
        merchant = Merchant.query.get_or_404(merchant_id)
        return merchant_schema.dump(merchant)

    def patch(self, merchant_id):
        merchant = Merchant.query.get_or_404(merchant_id)

        if 'name' in request.json:
            merchant.name = request.json['name']
        if 'description' in request.json:
            merchant.description = request.json['description']
        db.session.commit()
        return merchant_schema.dump(merchant)

    def delete(self, merchant_id):
        merchant = Merchant.query.get_or_404(merchant_id)
        db.session.delete(merchant)
        db.session.commit()
        return '', 204

api.add_resource(MerchantResource, '/merchants/<int:merchant_id>')

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(
                first_name=request.json['first_name'],
                last_name=request.json['last_name'],
                dob=request.json['dob'],
                timestamp  = datetime.now()
                )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

api.add_resource(UserListResource, '/users/')

class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        m = Merchant.query.get_or_404(1)
        print(m)
        return user_schema.dump(user)

api.add_resource(UserResource, "/users/<int:user_id>")

class TransactionListResource(Resource):

    def get(self):
        transactions = Transactions.query.all()
        return transactions_schema.dump(transactions)

api.add_resource(TransactionListResource, "/transactions/")

class TransactionResource(Resource):

    def post(self, user_id, merchant_id):
        merchant = Merchant.query.get(merchant_id)
        user = User.query.get(merchant_id)

        if merchant == None or user == None:
            return "User or Merchant not found", 404

        new_transaction = Transactions(
                description=request.json['description'],
                amount=request.json['amount'],
                credit=request.json['credit'],
                debit=request.json['debit'],
                user_id=user_id,
                merchant_id=merchant.id,
                timestamp = datetime.now()                )

        db.session.add(new_transaction)
        db.session.commit()
        return transaction_schema.dump(new_transaction)

api.add_resource(TransactionResource, '/transactions/users/<int:user_id>/merchants/<int:merchant_id>')

if __name__ == "__main__":
    app.run()

