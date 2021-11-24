from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)


# models
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Boolean)
    debit  = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref=db.backref('transactions', lazy=True))
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'), nullable=False)
    merchant = db.relationship("Merchant", backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f'Transaction: {self.description}'

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description  = db.Column(db.String(255))

    def __repr__(self):
        return f'Merchant Name: {self.name}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(16))

    def __repr__(self):
        return f'User Name: {self.first_name} {self.last_name}'


# schema
class MerchantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Merchant

merchant_schema = MerchantSchema()
merchants_schema = MerchantSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "dob")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
                description = request.json['description']
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
        try:
            merchant = Merchant.query.get_or_404(merchant_id)
            user = User.query.get_or_404(user_id)
        except:
            return "User or Merchant not found", 404

        new_transaction = Transactions(
                description=request.json['description'],
                amount=request.json['amount'],
                credit=request.json['credit'],
                debit=request.json['debit'],
                user_id=user.id,
                merchant_id=merchant.id
                )
        db.session.add(new_transaction)
        db.session.commit()
        return transaction_schema.dump(new_transaction)

api.add_resource(TransactionResource, '/transactions/users/<int:user_id>/merchants/<int:merchant_id>')
app.run()
