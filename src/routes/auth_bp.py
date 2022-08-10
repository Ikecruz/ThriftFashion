from flask import Blueprint
from controllers.auth_controller import index, register , verify

authBlueprint = Blueprint('authBlueprint', __name__)

authBlueprint.route('/', methods=['GET'])(index)
authBlueprint.route('/register', methods=['GET','POST'])(register)
authBlueprint.route('/verify', methods=['GET','POST'])(verify)