from database.db import db
def index():
    db.create_all()
    return "User"