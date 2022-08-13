from calendar import c
from itertools import product

from datetime import datetime
from database.db import db
from models.product_model import Product
class Cart (db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship( "Product")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    price= db.Column(db.Numeric,nullable=False)
    quantity= db.Column(db.Numeric,nullable=False)
    date_added = db.Column(db.DateTime(timezone=True),
                           nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<id %r>' % self.id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.merge(self)
        db.session.commit()
    def delete (self):
        db.session.delete(self)
        db.session.commit()
    

