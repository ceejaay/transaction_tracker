import uuid
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
DATABASE_URI = 'postgresql+psycopg2://cjem:password@localhost/homework_dev'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)


# models
# class Transactions(db.Model):
#     __tablename__ ='transactions'
#     id = db.Column(UUID(as_uuid=True), primary_key=True)
#     description = db.Column(db.String(50), nullable=False)
#     amount = db.Column(db.Integer, nullable=False)
#     credit = db.Column(db.Boolean)
#     debit  = db.Column(db.Boolean)
#     inserted_at = db.Column(db.DateTime),
#     updated_at = db.Column(db.DateTime)
# # relations
#     user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
#     users = db.relationship("Users", backref=db.backref('transactions', lazy=True))
#     merchant_id = db.Column(UUID, db.ForeignKey('merchant.id'), nullable=False)
#     merchant = db.relationship("Merchants", backref=db.backref('transactions', lazy=True))

#     def __repr__(self):
#         return f'Transaction: {self.description}'

class Merchants(db.Model):
    __tablename__ ='merchants'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description  = db.Column(db.String(255))
    inserted_at = db.Column(db.DateTime, nullable=False),
    updated_at = db.Column(db.DateTime, nullable=False)
    # relations
    # transaction = db.relationship("Transactions", back_populates="merchants", uselist=False)

    def __repr__(self):
        return f'Merchant Name: {self.name}'

class Users(db.Model):
    __tablename__ ='users'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(16))
    inserted_at = db.Column(db.DateTime, nullable=False),
    updated_at = db.Column(db.DateTime, nullable=False)

# relations
    # transaction = db.relationship("Transactions", back_populates="users", uselist=False)
    def __repr__(self):
        return f'User Name: {self.first_name} {self.last_name}'


# schema
class MerchantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Merchants

merchant_schema = MerchantSchema()
merchants_schema = MerchantSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "dob")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# class TransactionSchema(ma.Schema):
#     class Meta:
#         fields = (
#                 "id",
#                 "description",
#                 "amount",
#                 "credit",
#                 "debit",
#                 "user_id",
#                 "merchant_id",
#                 )

# transaction_schema = TransactionSchema()
# transactions_schema = TransactionSchema(many=True)

# resources


class MerchantListResource(Resource):
    def get(self):
        merchants = Merchants.query.all()
        return merchants_schema.dump(merchants)

    def post(self):
        new_merchant = Merchants(
                id=uuid.uuid1(),
                name=request.json['name'],
                description = request.json['description'],
                inserted_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S'),
                updated_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S')
        )
        db.session.add(new_merchant)
        db.session.commit()
        return merchant_schema.dump(new_merchant)

api.add_resource(MerchantListResource, '/api/v0/merchants/')

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

api.add_resource(MerchantResource, '/api/v0/merchants/<int:merchant_id>')

class UserListResource(Resource):
    def get(self):
        users = Users.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = Users(
                id=uuid.uuid1(),
                first_name=request.json['first_name'],
                last_name=request.json['last_name'],
                dob=request.json['dob'],
                inserted_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S'),
                updated_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S')
                )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

api.add_resource(UserListResource, '/api/v0/users/')

class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        m = Merchant.query.get_or_404(1)
        print(m)
        return user_schema.dump(user)

api.add_resource(UserResource, "/api/v0/users/<int:user_id>")

# class TransactionListResource(Resource):

#     def get(self):
#         transactions = Transactions.query.all()
#         return transactions_schema.dump(transactions)

# api.add_resource(TransactionListResource, "/api/v0/transactions/")

# class TransactionResource(Resource):

#     def post(self, user_id, merchant_id):
#         merchant = Merchant.query.get(merchant_id)
#         user = User.query.get(merchant_id)

#         if merchant == None or user == None:
#             return "User or Merchant not found", 404

#         new_transaction = Transactions(
#                 description=request.json['description'],
#                 amount=request.json['amount'],
#                 credit=request.json['credit'],
#                 debit=request.json['debit'],
#                 user_id=user_id,
#                 merchant_id=merchant.id,
#                 inserted_at = datetime.now(),
#                 updated_at = datetime.now()
#                 )

#         db.session.add(new_transaction)
#         db.session.commit()
#         return transaction_schema.dump(new_transaction)

# api.add_resource(TransactionResource, '/api/v0/transactions/users/<int:user_id>/merchants/<int:merchant_id>')

# class UserTransactionList(Resource):

#     def get(self, user_id):
#         transactions = Transactions.query.filter_by(user_id=user_id)
#         return transactions_schema.dump(transactions)

# api.add_resource(UserTransactionList, '/api/v0/users/<int:user_id>/transactions/')

# class MerchantTransactionsList(Resource):

#     def get(self, merchant_id):
#         transaction = Transactions.query.filter_by(merchant_id=merchant_id)
#         return transactions_schema.dump(transaction)


# api.add_resource(MerchantTransactionsList, '/api/v0/merchants/<int:merchant_id>/transactions/')


# app.run()
