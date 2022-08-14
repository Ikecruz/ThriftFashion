from flask import Blueprint
from controllers.main_controller import about, checkoutpage, contact, index as mainIndex, products

mainBlueprint = Blueprint('mainBlueprint', __name__)

mainBlueprint.route('/', methods=['GET'])(mainIndex)
mainBlueprint.route('/about', methods=['GET','POST'])(about)
mainBlueprint.route('/contact-us', methods=['GET','POST'])(contact)
mainBlueprint.route('/shop', methods=['GET','POST'])(products)
mainBlueprint.route('/checkout', methods=['GET','POST'])(checkoutpage)