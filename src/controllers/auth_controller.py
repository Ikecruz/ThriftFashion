from flask import redirect, request, render_template
from flask import session
from services.auth_services import emailExists, register_logic, usernameExists

def index():
    return redirect('/')
    
def register():
    error = ""
    if request.method == "POST" and 'submit' in request.form:

        body = request.form.get


        if (body('email') == "" or body('name') == "" or body('password') == "" or body('username') == "" ):
            error = "All fields are required"

        elif (emailExists(body('email'))):
            error = "Email already registered"

        elif (usernameExists(body('username'))):
            error = "Username already in use"

        else:
            if(register_logic(body)) :
                session['email'] = body('email')
                return redirect("/auth/verify")

    return render_template('register.html', error)