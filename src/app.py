from flask import Flask
from flask_migrate import Migrate
from database.db import db
from routes.auth_bp import authBlueprint
from routes.user_bp import userBlueprint
from routes.main_bp import mainBlueprint
from routes.product_bp import productBlueprint
from routes.admin_bp import adminBlueprint
from routes.cart_bp import cartBlueprint
from routes.feedback_bp import feedbackBlueprint
from routes.wishlist_bp import wishBlueprint
from flask_mail import Mail

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    return app

app = create_app()

app.register_blueprint(mainBlueprint, url='/')
app.register_blueprint(authBlueprint, url_prefix='/auth')
app.register_blueprint(userBlueprint, url_prefix="/my")
app.register_blueprint(productBlueprint,url_prefix='/product')
app.register_blueprint(adminBlueprint,url_prefix='/admin')
app.register_blueprint (cartBlueprint,url_prefix='/cart')
app.register_blueprint (feedbackBlueprint,url_prefix='/feedback')
app.register_blueprint(wishBlueprint, url_prefix='/wish')


migrate = Migrate(app, db)
# db.create_all(app=app)
mail = Mail(app)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
      