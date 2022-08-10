from datetime import datetime
from database.db import db

class users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    token = db.Column(db.String(80), nullable=False)
    email_verified = db.Column(db.String(80), nullable=False)
    join_date = db.Column(db.DateTime(timezone=True), server_default=datetime.utcnow())

    def __repr__(self):
        return '<id %r>' % self.id