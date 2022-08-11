from flask import redirect, request, render_template, session, jsonify
from services.auth_services import emailExists, register_logic, tokenExists, usernameExists, verify_logic

def index():
    return redirect('/')
    
def register():
    msg = ""
    if request.method == "GET":
        return render_template('register.html')

    if request.method == "POST":

        body = request.form.get

        if (body('email') == "" or body('name') == "" or body('password') == "" or body('username') == "" ):
            msg = "All fields are required"

        elif (emailExists(body('email'))):
            msg = "Email already registered"

        elif (usernameExists(body('username'))):
            msg = "Username already in use"

        else:
            if(register_logic(body)) :
                session['email'] = body('email')
                return jsonify({ 'status': "success" })

    return jsonify({ 'status': "error", 'message': msg })

def verify():
    if request.method == "GET":
        return render_template('verify.html')
