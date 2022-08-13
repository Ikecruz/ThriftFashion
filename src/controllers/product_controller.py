import re
from utils.file_util import upload_file
from services.product_service import add_category, add_product, categoryExists, getCategories, fetchProducts, productExists, update_stock
from services.email_services import sendEmail

from flask import jsonify, redirect, render_template, request, session, url_for


def index():
    if 'admin' not in session:
        return redirect('/admin/login')
    return render_template("admin/products.html")


def addProduct():
    if request.method == "POST":
        body = request.form.get
        f = request.files.get
        if (body("name") is None or body("price") is None or body("qty") is None or body("category") is None or body("description") is None or f('image') is None or body("gender") is None):
            msg = "Fill All fields"
            return jsonify({'status': "error", 'message': msg})
        elif 'admin' not in session:
                return redirect('/admin/login')
        elif productExists(body("name")):
            msg = "Product Name is in use"
            return jsonify({'status': "error", 'message': msg})
        elif categoryExists(body("category")) == False:
            msg = "Category Does Not Exist"
            return jsonify({'status': "error", 'message': msg})
        else:
            imgname = upload_file(f("image"))
            if imgname is None:
                msg = 'Error uploading file'
                return jsonify({'status': "error", 'message': msg})
            elif add_product(body, imgname):
                return jsonify({'status': "success"})
            else:
                return jsonify({'status': "error"})

def getCategory ():
    if request.method == "GET":
        data = []
        for cat in getCategories():
            data.append(
                {
                    'id': cat.id,
                    'name': cat.name
                }
            )
        
        print(data)
        return jsonify({'status':'success','data':data})


def getProducts():
    if request.method == "GET":
        data = []
        for prod in fetchProducts():
            data.append(
                {
                    'id': prod.id,
                    'name': prod.name,
                    'description':prod.description,
                    'quantity':prod.qty,
                    'category':prod.category.name,
                    'price':prod.price,
                    'img':prod.img_url
                }
            )

        print(data)
        return jsonify({'status': 'success', 'data': data})
def addCategory():
    if request.method == "POST":
        body = request.form.get
        if (body("name") is None):
            msg = "Fill All fields"
        # elif 'admin' not in session:
        #     return redirect('/admin/login')
        elif categoryExists(body("category")):
            msg = "Category Already  Exist"
        else:
            if add_category(body):
                return jsonify({'status': "success"})
    return jsonify({'status': "error", 'message': msg})


def updateStock ():
    if request.method == "POST":
        body = request.form.get
        if (body("name") is None or body ("qty")is None):
            msg = "Fill All fields"
        if 'admin' not in session:
            return redirect('/admin/login')
        elif productExists(body("name")) == False: 
            msg = "Product Not Found"  
        else : 
            if update_stock(body):
                return jsonify({'status': "success"})
                    
    return jsonify({'status': "error", 'message': msg})
