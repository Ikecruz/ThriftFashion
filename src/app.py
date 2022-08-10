from flask import Flask
from flask_migrate import Migrate
from database.db import db
from routes.auth_bp import authBlueprint
from routes.user_bp import userBlueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    return app


app = create_app()

app.register_blueprint(authBlueprint, url_prefix='/auth')
app.register_blueprint(userBlueprint, url_prefix="/user")

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)