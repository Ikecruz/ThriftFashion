

from services.cart_services import deleteProductInCart
from controllers.cart_controller import addToCart, cancelOrder, checkOut, removeFromCart
from flask import Blueprint


cartBlueprint = Blueprint('cartBlueprint',__name__)

cartBlueprint.route('/add',methods=['POST'])(addToCart)
cartBlueprint.route('/delete',methods=['POST'])(removeFromCart)
cartBlueprint.route('/update',methods=['POST'])(removeFromCart)
cartBlueprint.route('/checkout',methods=['POST'])(checkOut)
cartBlueprint.route('/cancel',methods=['POST'])(cancelOrder)