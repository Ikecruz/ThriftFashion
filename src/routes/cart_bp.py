

from controllers.cart_controller import addToCart
from flask import Blueprint


cartBlueprint = Blueprint('cartBlueprint',__name__)

cartBlueprint.route('/add',methods=['POST'])(addToCart)