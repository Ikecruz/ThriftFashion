
from services.wishlist_services import getAllWishes
from controllers.wishlist_controller import addToList, deleteFromWish, getWish
from flask import Blueprint


wishBlueprint = Blueprint('wishBlueprint', __name__)

wishBlueprint.route('/add', methods=['POST'])(addToList)
wishBlueprint.route('/delete', methods=['POST'])(deleteFromWish)
wishBlueprint.route('/get', methods=['GET'])(getWish)
