from models.feedback_model import Feedback


def addToFeedback (body):
    feedback = Feedback (
        email=body('email'),
        message=body('message'),
        name=body('name'),
        number=body('number')
    )

    try:
        Feedback.insert(feedback)
        return True
    except Exception as e:
        print(e)
        return False


def allFeedbacks ():
    feedbacks = Feedback.query.all()

    if feedbacks is None:
        return []
    data = []
    for feedback in feedbacks:
     data.append({
         'id':feedback.id,
         'name': feedback.name,
        'email': feedback.email,
        'number': feedback.number,
        'message':feedback.message
    })
    return data
