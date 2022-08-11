from flask import Blueprint
from controllers.auth_controller import forgot_password, index, register, resendOTP , verify, login

authBlueprint = Blueprint('authBlueprint', __name__)

authBlueprint.route('/', methods=['GET'])(index)
authBlueprint.route('/login', methods=['GET','POST'])(login)
authBlueprint.route('/register', methods=['GET','POST'])(register)
authBlueprint.route('/verify', methods=['GET','POST'])(verify)
authBlueprint.route('/resend-token', methods=['GET','POST'])(resendOTP)
authBlueprint.route('/forgot-password', methods=['GET','POST'])(forgot_password)