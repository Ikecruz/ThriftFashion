from flask import redirect, request, render_template, session, jsonify
from services.auth_services import emailExists, register_logic, resendToken, usernameExists, verify_logic

def index():
    return redirect('/')
    
def register():
    msg = ""

    if request.method == "POST":

        body = request.form.get

        if (body('email') == "" or body('name') == "" or body('password') == "" or body('username') == "" ):
            msg = "All fields are required"
            return jsonify({ 'status': "error", 'message': msg })

        elif (emailExists(body('email'))):
            msg = "Email already registered"
            return jsonify({ 'status': "error", 'message': msg })

        elif (usernameExists(body('username'))):
            msg = "Username already in use"
            return jsonify({ 'status': "error", 'message': msg })

        else:
            if(register_logic(body)) :
                session['temp_email'] = body('email')
                return jsonify({ 'status': "success" })

    return render_template('register.html')

def verify():
    if 'temp_email' in session:
        email = session['temp_email']

        if request.method == "POST":
            body = request.form.get

            if (body('vcode') == ""):
                msg = "All fields are required"
                jsonify({'status': "success", 'message': msg})

            else:
                if verify_logic(email, body('vcode')):
                    session.pop("temp-email", None)
                    return jsonify({ 'status': "success", 'message': "verified" })
        else:
            return render_template('verify.html')
    else :
        return redirect("/")

def resendOTP():

    if 'temp_email' in session:

        email = session['temp_email']

        if(resendToken(email)):
            return jsonify({ 'status': "success"})

    return jsonify({ 'status': "error" })