import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('cook_book')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)   

@app.route('/')
@app.route('/products')
def index():
    return render_template("products.html", products=mongo.db.products.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)