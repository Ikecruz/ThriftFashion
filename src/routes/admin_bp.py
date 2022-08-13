from flask import Blueprint
from controllers.admin_controller import index, orders, register, login, products, product, users,user


adminBlueprint = Blueprint('adminBlueprint', __name__)

adminBlueprint.route('/', methods=['GET'])(index)
adminBlueprint.route('/orders', methods=['GET'])(orders)
adminBlueprint.route('/users', methods=['GET'])(users)
adminBlueprint.route('/user/<int:id>', methods=['GET'])(user)
adminBlueprint.route('/register', methods=['POST'])(register)
adminBlueprint.route('/login', methods=['GET','POST'])(login)
adminBlueprint.route('/products', methods=['GET'])(products)
adminBlueprint.route('/add-product', methods=['GET'])(product)
