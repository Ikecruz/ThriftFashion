from flask import Blueprint
from controllers.product_controller import addCategory, addProduct, index, updateStock


productBlueprint = Blueprint("productBlueprint",__name__)
productBlueprint.route('/', methods=['POST'])(index)
productBlueprint.route('/add', methods=['POST'])(addProduct)
productBlueprint.route('/update', methods=['POST'])(updateStock)
productBlueprint.route('/category/add', methods=['POST'])(addCategory)