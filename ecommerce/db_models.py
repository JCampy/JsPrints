from flask import Flask
from flask import Blueprint
from . import db
from flask_login import UserMixin
from random import *

db_models = Blueprint('db_models', __name__)

# Database setup 

# create database tables if or check if they exist. 
#    class login(db.Model):
#        num_of_acc = db.Column(db.Integer, primary_key=True)
#        user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#        password = db.Column(db.String(255))
#
#        def __init__(self, user_id, password):
#            self.user_id = user_id
#            self.password = password

# user table
class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    user_email = db.Column(db.String(100), unique=True)
    user_fname = db.Column(db.String(50))
    user_lname = db.Column(db.String(50))
    password = db.Column(db.String(300))
    user_phone_num = db.Column(db.String(50), nullable=True)
    user_address = db.Column(db.String(255), nullable=True)
    products = db.relationship('Product', backref='products')
    purchase_history = db.relationship('Purchase_history', backref='purchase_his')
    payments = db.relationship('Payment', backref='payments')
    cart = db.relationship('Cart', backref='cart')
    orders =db.relationship("Orders", backref='orders')
    shipping = db.relationship("Shipping", backref='shipping')

    def __init__(self, user_name, user_email, user_fname, user_lname, password, user_phone_num):
        self.user_name = user_name
        self.user_email = user_email
        self.user_fname = user_fname
        self.user_lname = user_lname
        self.password = password
        self.user_phone_num = user_phone_num
        
    
    def get_id(self):
        return self.user_id

# shopping cart table
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)
    products = db.relationship("Product", backref='cart_prod')

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.payment_id'))
    shipping_addr = db.Column(db.String(300))
    billing_addr = db.Column(db.String(300))
    orderedproduct = db.relationship("OrderedProduct", backref='ordered')

    def __init__(self, user_id, fname, lname, user_email, payment_id, shipping_addr, billing_addr):
        self.order_id = getrandbits(16)
        self.user_id = user_id
        self.fname = fname
        self.lname = lname
        self.user_email = user_email
        self.payment_id = payment_id
        self.shipping_addr = shipping_addr
        self.billing_addr = billing_addr

class OrderedProduct(db.Model):
    ordered_prod_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

# product table
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    prod_desc = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    prod_price = db.Column(db.Float)
    category = db.Column(db.String(50))
    filename = db.Column(db.String(500))
    orderedproduct = db.relationship("OrderedProduct", backref='prod_ordered')
    purchase_history = db.relationship('Purchase_history', backref='prod_his')
    #prod_img = db.Column(db.LargeBinary)

    def __init__(self, product_name, prod_desc, user_id, prod_owner, category, prod_price, filename):
        #self.product_id = product_id
        self.product_name = product_name
        self.prod_desc = prod_desc
        self.user_id = user_id
        self.prod_owner = prod_owner
        self.category = category
        self.prod_price = prod_price
        self.filename = filename
        #self.prod_img = prod_img

# shipping info table
class Shipping(db.Model):
    shipping_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    shipping_addr = db.Column(db.String(255))

    def __init__(self, user_id, shipping_addr):
        self.user_id = user_id
        self.shipping_addr = shipping_addr

# payment info table
class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    card_num = db.Column(db.String(16))
    card_holder_name = db.Column(db.String(255))
    card_exp = db.Column(db.Integer)
    card_pin = db.Column(db.Integer)
    billing_addr = db.Column(db.String(255))

    def __init__(self, user_id, card_num, card_holder_name, card_exp, card_pin, billing_addr):
        self.user_id = user_id
        self.card_num = card_num
        self.card_holder_name = card_holder_name
        self.card_exp = card_exp
        self.card_pin = card_pin
        self.billing_addr = billing_addr

# purchase history table
class Purchase_history(db.Model):
    purchase_history_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quanity = db.Column(db.Integer)
    purchase_date = db.Column(db.String(64))
    transaction_cost = db.Column(db.Float)

    def __init__(self, user_id, product_id, quanity, purchase_price, transaction_cost):

        self.user_id = user_id
        self.product_id = product_id
        self.quanity = quanity
        self.purchase_price = purchase_price
        self.transaction_cost = transaction_cost

    