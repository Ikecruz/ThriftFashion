from flask import Blueprint
from controllers.auth_controller import index as authIndex, register as authRegister

authBlueprint = Blueprint('authBlueprint', __name__)

authBlueprint.route('/', methods=['GET'])(authIndex)
authBlueprint.route('/register', methods=['GET','POST'])(authRegister)