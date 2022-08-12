from services.user_services import check_password, getUserDetail, updateUserDetail, updatepassword_logic
from flask import session, redirect, request, render_template, jsonify

def index():
    return "User"

def profile():
    if "user_email" in session:
        user_email = session["user_email"]
        
        if request.method == "GET":
            data = getUserDetail(user_email)
            if (data):
                return render_template("user/details.html", user_profile=data)
            else:
                return redirect("/")
        
        if request.method == "POST":
            msg = ""

            body = request.form.get
            if body('name') is None and body('number') is None:
                msg = "All fields are required"
                return jsonify({ 'status': "error", 'message': msg })
            
            if updateUserDetail(user_email, body):
                return jsonify({ 'status': "success"})
            else:
                msg = "An Error occurred"
                return jsonify({ 'status': "error", 'message': msg })
    else:
        return redirect("/")

def change_password():
    if "user_email" in session:
        user_email = session["user_email"]
        
        if request.method == "GET":
            return render_template('user/change-password.html')
        
        if request.method == "POST":
            body = request.form.get

            if body('new_pass') is None and body('old_pass') is None:
                msg = "All fields are required"
                return jsonify({'status': "error",'message': msg })
            
            if not check_password(user_email, body('old_pass')):
                msg = "Old Password Incorrect"
                return jsonify({'status': "error",'message': msg })
            else:
                if updatepassword_logic(user_email, body('new_pass')):
                    return jsonify({'status': "success"})
                else:
                    msg = "Update Error"
                    return jsonify({'status': "error",'message': msg })

    else:
        return redirect("/")