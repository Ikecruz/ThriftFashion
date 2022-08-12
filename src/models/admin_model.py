from datetime import datetime
from database.db import db


class Admin(db.Model):

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    join_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return '<id %r>' % self.id

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.merge(self)
        db.session.commit()