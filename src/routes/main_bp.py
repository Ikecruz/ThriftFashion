from flask import Blueprint
from controllers.main_controller import index as mainIndex

mainBlueprint = Blueprint('mainBlueprint', __name__)

mainBlueprint.route('/', methods=['GET'])(mainIndex)