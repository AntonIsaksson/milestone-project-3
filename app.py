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


@app.route('/lists')
def show_lists():
    return render_template("lists.html",
                            lists=list(mongo.db.lists.find()))


@app.route('/show_list')
def show_list():
    return render_template("show_list.html", 
                            lists=list(mongo.db.lists.find()))


@app.route('/create_list')
def create_list():
    return render_template("create_list.html",
                            lists=list(mongo.db.lists.find()))



@app.route('/insert_list_name', methods=['POST'])
def insert_list_name():
    list_name = {'list_name': request.form.get('list_name')}
    mongo.db.lists.insert_one(list_name)                       



if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)
