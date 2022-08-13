from services.user_services import blockuser_logic, unblockuser_logic
from flask import redirect, request, render_template, session, jsonify
from services.auth_services import changepassword_logic, emailExists, login_logic, register_logic, resendToken, usernameExists, verify_logic

def index():
    return redirect('/')
    

def register():
    msg = ""

    if request.method == "POST":

        body = request.form.get

        if (body('email') is None or body('name') is None or body('password') is None or body('username') is None ):
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

    return render_template('auth/register.html')


def verify():
    if 'temp_email' in session:
        email = session['temp_email']

        if request.method == "POST":
            body = request.form.get

            if (body('vcode') is None):
                msg = "All fields are required"
                return jsonify({'status': "error", 'message': msg})

            else:
                if verify_logic(email, body('vcode')):
                    if request.args.get('changepassword') is not None:
                        session["changepass-email"] = email

                    session.pop("temp-email", None)
                    return jsonify({ 'status': "success", 'message': "verified" })
        else:
            return render_template('auth/verify.html')
    else :
        return redirect("/")


def resendOTP():

    if 'temp_email' in session:

        email = session['temp_email']

        if(resendToken(email)):
            return jsonify({ 'status': "success"})

    return jsonify({ 'status': "error" })


def login():

    msg = ""

    if (request.method == "POST"):
        body = request.form.get

        if (body('email') is None or body('password') is None ):
            msg = "All fields are required"
            return jsonify({ 'status': "error", 'message': msg })
        
        if (login_logic(body)):
            user_id = login_logic(body)
            session['key'] = user_id
            return jsonify({'status': "success"})
        else:
            msg = "Login details are incorrect"
            return jsonify({ 'status': "error", 'message': msg })
    
    return render_template('auth/login.html')


def forgot_password():
    
    if request.method == "POST":
        body = request.form.get

        if (body('email') is None):
            msg = "Email is required"
            return jsonify({'status': "error",'message': msg })

        if (resendToken(body('email'))):
            session['temp_email'] = body('email')
            return jsonify({'status': "success"})
        else: 
            return redirect("/auth/signup")

    return render_template('auth/forgotpassword.html')


def changePass():
    msg = ""

    if "changepass-email" in session:
        email = session["changepass-email"]

        if request.method == "POST":
            body = request.form.get

            if (body('password') is None):
                msg = "Password is required"
                return jsonify({'status': "error",'message': msg })

            if (changepassword_logic(email, body('password'))):
                session.pop('changepassword-email', None)
                return jsonify({'status': "success"})
        else:
            return render_template('auth/changepassword.html')

    return redirect("/auth/register")

def block():
    if request.method == "POST":
        body = request.form.get

        if (body('id') is None):
            msg = "id is required"
            return jsonify({'status': "error",'message': msg })
        else :
            if blockuser_logic(body ('id')) :
             return jsonify({'status': "success"})
        return jsonify({'status': "error"})   
def unblock():
    if request.method == "POST":
        body = request.form.get

        if (body('id') is None):
            msg = "id is required"
            return jsonify({'status': "error",'message': msg })
        else :
            if unblockuser_logic(body ('id')) :
             return jsonify({'status': "success"})
        return jsonify({'status': "error"})           