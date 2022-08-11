import re
from utils.file_util import upload_file
from services.product_service import add_category, add_product, categoryExists, productExists, update_stock
from services.email_services import sendEmail

from flask import jsonify, redirect, request, session, url_for


def index():
    return ""


def addProduct():
    if request.method == "POST":
        body = request.form.get
        f = request.files.get
        if (body("name") == "" or body("price") == "" or body("qty") == "" or body("category") == "" or f('image') == None):
            msg = "Fill All fields"
        if 'admin' not in session:
                return redirect('/admin/login')
        elif productExists(body("name")):
            msg = "Product Name is in use"
        elif categoryExists(body("category")) == False:
            msg = "Category Does Not Exist"
        else:
            imgname = upload_file(f("image"))
            if imgname == "":
                msg = 'Error uploading file'
            elif add_product(body, imgname):
                return jsonify({'status': "error"})
            else:
                return jsonify({'status': "error"})
    return jsonify({'status': "error", 'message': msg})


def addCategory():
    if request.method == "POST":
        body = request.form.get
        if (body("name") == ""):
            msg = "Fill All fields"
        if 'admin' not in session:
            return redirect('/admin/login')
        elif categoryExists(body("category")):
            msg = "Category Already  Exist"
        else:
            if add_category(body):
                return jsonify({'status': "success"})
    return jsonify({'status': "error", 'message': msg})


def updateStock ():
    if request.method == "POST":
        body = request.form.get
        if (body("name") == "" or body ("qty")==""):
            msg = "Fill All fields"
        if 'admin' not in session:
            return redirect('/admin/login')
        elif productExists(body("name")) == False: 
            msg = "Product Not Found"  
        else : 
            if update_stock(body):
                return jsonify({'status': "success"})
                    
    return jsonify({'status': "error", 'message': msg})
