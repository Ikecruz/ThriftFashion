from datetime import datetime
from email.policy import default
from database.db import db


class Product (db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric())
    img_url = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category")
    qty = db.Column(db.Integer(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), nullable=False,default=datetime.now)
    gender = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id
    def insert(self):
        db.session.add(self)
        db.session.commit() 
    def update(self):
        db.session.merge(self)
        db.session.commit()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<id %r>' % self.id

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.merge(self)
        db.session.commit()    
