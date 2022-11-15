from services.feedback_services import addToFeedback, allFeedbacks
from flask import jsonify, request


def newMessage ():
    if request.method=="POST":
        body=request.form.get
        if (body('email') is None or body('name') is None or body('number') is None or body('message') is None ):
                msg = "All fields are required"
                return jsonify({ 'status': "error", 'message': msg })

        else :
          if (addToFeedback(body)):
            return jsonify({ 'status': "success" })
          return jsonify({ 'status': "error" })   

def getFeedbacks ():
    if request.method=="GET":
        data = allFeedbacks()
        return jsonify({ 'status': "success",'feedbacks':data })   