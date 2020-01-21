import os
from flask import Flask, render_template, redirect, request, url_for
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
    return render_template("products/products.html", products=mongo.db.products.find())


# route to add a product / this will open an new web window 
@app.route('/add_product')
def add_product():
    return render_template('products/addproduct.html', products=mongo.db.products.find())

# this route will insert all the products input field into DB and return them in the product management page.
@app.route('/insert_product', methods=['POST'])
def insert_product():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for('products'))


# this will delete the data from products category/ will delete added products
# should use product insted products 'cuz im looping product inside products list in mongodb.
# only use products as mongodb to connect the DB to the page 
@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    mongo.db.products.remove({'_id': ObjectId(product_id)})
    return redirect(url_for('products'))


# this is the route to edit a product details

@app.route('/edit_product/<product_id>')
def edit_product(product_id):
  #  products = mongo.db.products
    products = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template('products/editproduct.html', product=products)


@app.route('/update_product/<product_id>', methods=["POST"])
def update_product(product_id):
    products = mongo.db.products
    products.update({"_id": ObjectId(product_id)},
    {
      'ref_number': request.form.get('ref_number'),
      'name': request.form.get('name'),
      'color': request.form.get('color'),
      'size': request.form.get('size'),
      'unit_price': request.form.get('unit_price'),
      'sale_price': request.form.get('sale_price')

    })

    return redirect(url_for('products'))


# -------------------------------------PODUCT STOCK MANAGEMENT----------------------------------------------

@app.route('/stock')
def stock():
    return render_template("stock/stock.html", stock=mongo.db.stock.find())

# route to add a stock / this will open an new web window 
@app.route('/add_stock')
def add_stock():
    return render_template('stock/addstock.html', stock=mongo.db.stock.find())

# this route will insert all the products input field into DB and return them in the product management page.
@app.route('/insert_stock', methods=['POST'])
def insert_stock():
    stock = mongo.db.stock
    stock.insert_one(request.form.to_dict())
    return redirect(url_for('stock'))

# this will delete the data from STOCK category/ will delete added products
# should use ITEMS insted STOCK 'cuz im looping ITEMS inside STOCK list in mongodb.
# only use STOCK as mongodb to connect the STOCK in mongoDB. 
@app.route('/delete_stock/<items_id>')
def delete_stock(items_id):
    mongo.db.stock.remove({'_id': ObjectId(items_id)})
    return redirect(url_for('stock'))


# this is the route to edit a STOCK details

@app.route('/edit_stock/<items_id>')
def edit_stock(items_id):
    stock = mongo.db.stock.find_one({"_id": ObjectId(items_id)})
    return render_template('stock/editstock.html', items=stock)


@app.route('/update_stock/<items_id>', methods=["POST"])
def update_stock(items_id):
    stock = mongo.db.stock
    stock.update({"_id": ObjectId(items_id)},{'ref_number': request.form.get('ref_number'),
                                              'stock_inward': request.form.get('stock_inward'),
                                              'stock_outward': request.form.get('stock_outward'),
                                              'stock_total': request.form.get('stock_total')
    })

    return redirect(url_for('stock'))


# ---------------------------------------CLIENTS ROUTE ------------------------------------------------------


@app.route('/client')
def client():
    return render_template("client/client.html", clients=mongo.db.clients.find())

# route to add a CLIENT / this will open an new web window 
@app.route('/add_client')
def add_client():
    return render_template('client/addclient.html', clients=mongo.db.clients.find())

# this route will insert all the CLIENTS input field into DB and return them in the CLIENT MANAGEMENT PAGE.
@app.route('/insert_client', methods=['POST'])
def insert_client():
    clients = mongo.db.clients
    clients.insert_one(request.form.to_dict())
    return redirect(url_for('client'))

# this will delete the data from CLIENTS category/ will delete added CLIENTS
# should use SALE insted CLIENTS 'cuz im looping SALE inside CLIENTS list in mongodb.
# only use CLIENTS as mongodb to connect the CLIENTS in mongoDB. 
@app.route('/delete_client/<sale_id>')
def delete_client(sale_id):
    mongo.db.clients.remove({'_id': ObjectId(sale_id)})
    return redirect(url_for('client'))


# this is the route to edit a CLIENT details

@app.route('/edit_client/<sale_id>')
def edit_client(sale_id):
    clients = mongo.db.clients.find_one({"_id": ObjectId(sale_id)})
    return render_template('client/editclient.html', sale=clients)


@app.route('/update_client/<sale_id>', methods=["POST"])
def update_client(sale_id):
    clients = mongo.db.clients
    clients.update({"_id": ObjectId(sale_id)}, {'client_ref': request.form.get('client_ref'),
                                                'name': request.form.get('name'),
                                                'phone': request.form.get('phone'),
                                                'email': request.form.get('email'),
                                                'address': request.form.get('address')
    })

    return redirect(url_for('client'))




# -----------------------------------SUPPLIERS ROUTE--------------------------------------------------------


@app.route('/supplier')
def supplier():
    return render_template("suppliers/suppliers.html", supplier=mongo.db.supplier.find())

# route to add a CLIENT / this will open an new web window 
@app.route('/add_supplier')
def add_supplier():
    return render_template('suppliers/addsuppliers.html', supplier=mongo.db.supplier.find())

# this route will insert all the SUPPLIERS input field into DB and return them in the CUSTOMER MANAGEMENT PAGE.
@app.route('/insert_supplier', methods=['POST'])
def insert_supplier():
    supplier = mongo.db.supplier
    supplier.insert_one(request.form.to_dict())
    return redirect(url_for('supplier'))

# this will delete the data from SUPPLIER category/ will delete added SUPPLIERS
# should use BUY insted SUPPLIER 'cuz im looping BUY inside SUPPLIER list in mongodb.
# only use SUPPLIER as mongodb to connect the SUPPLIER in mongoDB. 
@app.route('/delete_supplier/<buy_id>')
def delete_supplier(buy_id):
    mongo.db.supplier.remove({'_id': ObjectId(buy_id)})
    return redirect(url_for('supplier'))


# this is the route to edit a SUPPLIERS details

@app.route('/edit_supplier/<buy_id>')
def edit_supplier(buy_id):
    supplier = mongo.db.supplier.find_one({"_id": ObjectId(buy_id)})
    return render_template('suppliers/editsuppliers.html', buy=supplier)


@app.route('/update_supplier/<buy_id>', methods=["POST"])
def update_supplier(buy_id):
    supplier = mongo.db.supplier
    supplier.update({"_id": ObjectId(buy_id)}, {'sup_ref': request.form.get('sup_ref'),
                                                'name': request.form.get('name'),
                                                'phone': request.form.get('phone'),
                                                'email': request.form.get('email'),
                                                'address': request.form.get('address')
    })

    return redirect(url_for('supplier'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)