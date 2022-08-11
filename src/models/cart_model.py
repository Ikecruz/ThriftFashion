from calendar import c
from itertools import product

from datetime import datetime
from database.db import db
class Cart (db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship( "Product", backref=db.backref("products", uselist=False))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref=db.backref("users", uselist=False))
    price= db.Column(db.Numeric,nullable=False)
    quantity= db.Column(db.Numeric,nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), nullable=False)
    

