from services.user_services import check_password, getUserDetail, updateUserDetail, updatepassword_logic
from flask import session, redirect, request, render_template, jsonify

def index():
    print(request.path)
    return render_template("user/index.html")

def profile():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            data = getUserDetail(key)
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
            
            if updateUserDetail(key, body):
                return jsonify({ 'status': "success"})
            else:
                msg = "An Error occurred"
                return jsonify({ 'status': "error", 'message': msg })
    else:
        return redirect("/")

def change_password():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            return render_template('user/change-password.html')
        
        if request.method == "POST":
            body = request.form.get

            if body('new_pass') is None and body('old_pass') is None:
                msg = "All fields are required"
                return jsonify({'status': "error",'message': msg })
            
            if not check_password(key, body('old_pass')):
                msg = "Old Password Incorrect"
                return jsonify({'status': "error",'message': msg })
            else:
                if updatepassword_logic(key, body('new_pass')):
                    return jsonify({'status': "success"})
                else:
                    msg = "Update Error"
                    return jsonify({'status': "error",'message': msg })

    else:
        return redirect("/")