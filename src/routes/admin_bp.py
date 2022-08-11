from flask import Blueprint
from controllers.admin_controller import index, register , login

adminBlueprint = Blueprint('adminBlueprint', __name__)

adminBlueprint.route('/', methods=['GET'])(index)
adminBlueprint.route('/register', methods=['GET', 'POST'])(register)
adminBlueprint.route('/login', methods=['GET','POST'])(login)