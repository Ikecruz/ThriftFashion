from database.db import db


class Product (db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric())
    img_url = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False,)
    category = db.relationship("Category", backref="product")
    date_added = db.Column(db.DateTime(timezone=True), nullable=False)
    def __repr__(self):
        return '<id %r>' % self.id


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

