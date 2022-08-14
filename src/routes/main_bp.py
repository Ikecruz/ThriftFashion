from flask import Blueprint
<<<<<<< HEAD
from controllers.main_controller import about, checkoutpage, contact, index as mainIndex, products
=======
from controllers.main_controller import about, contact, index as mainIndex, products, search, singleProduct
>>>>>>> d762d6166ac848cc2de642d27f92e3ca8f38e413

mainBlueprint = Blueprint('mainBlueprint', __name__)

mainBlueprint.route('/', methods=['GET'])(mainIndex)
mainBlueprint.route('/about', methods=['GET','POST'])(about)
mainBlueprint.route('/contact-us', methods=['GET','POST'])(contact)
mainBlueprint.route('/shop', methods=['GET','POST'])(products)
<<<<<<< HEAD
mainBlueprint.route('/checkout', methods=['GET','POST'])(checkoutpage)
=======
mainBlueprint.route('/product/<int:id>', methods=['GET','POST'])(singleProduct)
mainBlueprint.route('/search', methods=['GET','POST'])(search)
>>>>>>> d762d6166ac848cc2de642d27f92e3ca8f38e413
