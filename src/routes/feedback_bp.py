from controllers.feedback_controller import newMessage, getFeedbacks
from flask import Blueprint


feedbackBlueprint = Blueprint('feedbackBlueprint', __name__)

feedbackBlueprint.route('/add', methods=['POST'])(newMessage)
feedbackBlueprint.route('/all', methods=['GET'])(getFeedbacks)
