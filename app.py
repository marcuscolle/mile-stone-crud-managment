import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('management')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)   


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/products')
def products():
    return render_template("products.html", products=mongo.db.products.find())


# route to add a product / this will open an new web window 
@app.route('/add_product')
def add_product():
    return render_template('addproduct.html', products=mongo.db.products.find())

# this route will insert all the products input field into DB and return them in the product management page.
@app.route('/insert_product', methods=['POST'])
def insert_product():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for('products'))


# this will delete the data from products category/ will delete added products
#should use product insted products 'cuz im looping product inside products list in mongodb.
# only use products as mongodb to connect the DB to the page 
@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('products'))







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)