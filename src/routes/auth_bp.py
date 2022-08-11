from flask import Blueprint
from controllers.auth_controller import index, register, resendOTP , verify, login

authBlueprint = Blueprint('authBlueprint', __name__)

authBlueprint.route('/', methods=['GET'])(index)
authBlueprint.route('/login', methods=['GET','POST'])(login)
authBlueprint.route('/register', methods=['GET','POST'])(register)
authBlueprint.route('/verify', methods=['GET','POST'])(verify)
authBlueprint.route('/resend-token', methods=['GET','POST'])(resendOTP)