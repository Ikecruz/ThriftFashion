from database.db import db
def run():
    db.create_all()


if __name__ == "__main__":
    run()