from flask import Blueprint
from controllers.product_controller import addCategory, addProduct, getProducts, index, updateStock, getCategory


productBlueprint = Blueprint("productBlueprint",__name__)
productBlueprint.route('/', methods=['POST'])(index)
productBlueprint.route('/add', methods=['POST'])(addProduct)
productBlueprint.route('/get', methods=['GET'])(getProducts)
productBlueprint.route('/update', methods=['POST'])(updateStock)
productBlueprint.route('/category/add', methods=['POST'])(addCategory)
productBlueprint.route('/category/get', methods=['GET'])(getCategory)
