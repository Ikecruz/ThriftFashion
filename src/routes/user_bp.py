from flask import Blueprint
from controllers.user_controller import change_password, index, order, profile, wishlist

userBlueprint = Blueprint('userBlueprint', __name__)

userBlueprint.route('/', methods=['GET'])(index)
userBlueprint.route('/profile', methods=['GET','POST'])(profile)
userBlueprint.route('/settings', methods=['GET','POST'])(change_password)
userBlueprint.route('/order', methods=['GET','POST'])(order)
userBlueprint.route('/wishlist', methods=['GET','POST'])(wishlist)