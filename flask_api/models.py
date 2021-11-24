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
# models
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Boolean)
    debit  = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)

    # relashionships

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
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'Merchant Name: {self.name}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'User Name: {self.first_name} {self.last_name}'
