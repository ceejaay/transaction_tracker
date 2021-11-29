from flask_api import db

# models
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Boolean)
    debit  = db.Column(db.Boolean)
    inserted_at = db.Column(db.DateTime),
    updated_at = db.Column(db.DateTime)

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
    inserted_at = db.Column(db.DateTime),
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'Merchant Name: {self.name}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(16))
    inserted_at = db.Column(db.DateTime),
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'User Name: {self.first_name} {self.last_name}'

