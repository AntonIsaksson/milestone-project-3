import os
from flask import Flask, render_template, redirect, request, url_for
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# app.secret_key = os.getenv("SECRET", "mySecretKey")
app.config["MONGO_DBNAME"] = "topTenDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)



# Route to homepage
@app.route('/')
@app.route('/home')
def home_page():
    return render_template ("base.html")


@app.route('/show_categories')
def show_categories():
    return render_template("categories.html", 
                            categories=list(mongo.db.categories.find()))


@app.route('/lists')
def show_lists():
    return render_template("lists.html", 
                            categories=list(mongo.db.categories.find()),
                            lists=list(mongo.db.lists.find()),
                            list_object=list(mongo.db.list_object.find()))


@app.route('/create_list')
def create_list():
    return render_template("create_list.html", 
                            categories=list(mongo.db.categories.find()),
                            lists=list(mongo.db.lists.find()),
                            list_object=list(mongo.db.list_object.find()))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=list(mongo.db.categories.find()))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('create_list'))  


@app.route('/add_category')
def add_category():
    return render_template('add_category.html')                          



if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)
