from calendar import c
import email
from email import message
from itertools import product

from datetime import datetime
from database.db import db
from models.product_model import Product


class Feedback (db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    number = db.Column(db.String(45), nullable=False)
    message = db.Column(db.String(100), nullable=False)
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

    def delete(self):
        db.session.delete(self)
        db.session.commit()
