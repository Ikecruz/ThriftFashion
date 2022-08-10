from flask import Blueprint
from controllers.user_controller import index as userIndex

userBlueprint = Blueprint('userBlueprint', __name__)

userBlueprint.route('/', methods=['GET'])(userIndex)