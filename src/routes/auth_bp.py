from flask import Blueprint
from controllers.auth_controller import index as authIndex

authBlueprint = Blueprint('authBlueprint', __name__)

authBlueprint.route('/', methods=['GET'])(authIndex)