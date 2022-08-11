from flask_mail import  Message

def sendEmail(header, reciever, body):
    from app import mail
    
    msg = Message(header, sender="admin@diagnosisabc.com", recipients=[reciever])
    msg.body = body
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Failed to send email Error: {e}")
        return False