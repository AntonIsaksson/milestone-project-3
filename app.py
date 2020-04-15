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
                            categories=list(mongo.db.categories.find()))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)
