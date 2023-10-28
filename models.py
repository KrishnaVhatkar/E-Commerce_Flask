from flask_sqlalchemy import SQLAlchemy
from db import db
db = SQLAlchemy()

class User(db.Model):
	usr_id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(100), nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)
	def __repr__(self):
		return '<Name %r>' % self.fullname

class Product(db.Model):
	pro_id = db.Column(db.Integer, primary_key=True)
	category= db.Column(db.String(50), nullable=False)
	name = db.Column(db.String(100), nullable=False)
	description= db.Column(db.String(250), nullable=True)
	price_range= db.Column(db.String(200), nullable=False)
	comments= db.Column(db.String(200), nullable=True)
	filename = db.Column(db.Text, nullable=False, unique=True)
	username = db.Column(db.String(50), nullable=False)
	def __repr__(self):
		return '<Name %r>' % self.name


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.usr_id'))  # Update this line
    product_id = db.Column(db.Integer, db.ForeignKey('product.pro_id'))
    quantity = db.Column(db.Integer, default=1)

    user = db.relationship('User', back_populates='cart')
    product = db.relationship('Product', foreign_keys=[product_id])
