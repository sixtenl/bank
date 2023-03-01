from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__= 'Customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    street_address = db.Column(db.String(50), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    zipcode = db.Column(db.String(10), unique=False, nullable=False)
    country = db.Column(db.String(30), unique=False, nullable=False)
    country_code = db.Column(db.String(2), unique=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, nullable=False)
    national_id = db.Column(db.String(20), unique=False, nullable=False)
    telephone_country_code = db.Column(db.Integer, unique=False, nullable=False)
    telephone = db.Column(db.String(20), unique=False, nullable=False)
    email_address = db.Column(db.String(50), unique=False, nullable=False)
    accounts = db.relationship('Account', backref='Customer',lazy=True)

    def to_dict(self):
        accounts = self.accounts
        balance = 0
        for account in accounts:
            balance += account.balance
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'street_address': self.street_address,
            'city': self.city,
            'zipcode': self.zipcode,
            'country': self.country,
            'country_code': self.country_code,
            'birthday': self.birthday,
            'national_id': self.national_id,
            'telephone_country_code': self.telephone_country_code,
            'telephone': self.telephone,
            'email_address': self.email_address,
            'balance': balance
        }

class Account(db.Model):
    __tablename__= 'Accounts'
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(10), unique=False, nullable=False)
    created = db.Column(db.DateTime, unique=False, nullable=False)
    balance = db.Column(db.Integer, unique=False, nullable=False)
    transactions = db.relationship('Transaction', backref='Account', lazy=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.id'), nullable=False)

class Transaction(db.Model):
    __tablename__= 'Transactions'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=False, nullable=False)
    operation = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    new_balance = db.Column(db.Integer, unique=False, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('Accounts.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'operation': self.operation,
            'amount': self.amount,
            'new_balance': self.new_balance,
            'datetime': self.date
        }

class Role(db.Model):
    __tablename__ = 'Roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref='Role', lazy=True)

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50), unique=False, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not readable.')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

