
from re import I
from flask import Blueprint
from controllers.product_controller import index


productBlueprint = Blueprint("productBlueprint",__name__)
productBlueprint.route('/', methods=['POST'])(index)