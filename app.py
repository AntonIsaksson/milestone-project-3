import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
import bcrypt
import re
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY')
app.secret_key = os.environ.get('secret_key')
app.config["MONGO_DBNAME"] = "topTenDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
# Route to homepage
@app.route('/home')
def home_page():
    if 'username' in session:
        return render_template("home.html", users = mongo.db.users.find_one({'name': session['username']}))
    return render_template ("home.html")


@app.route('/to_login')
def to_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home_page'))
    return 'Invalid username/password combination'

@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # Kill session
    return redirect(url_for('home_page'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            session.clear()
            return redirect(url_for('to_login'))
        
        return 'That username already exists!'

    return render_template('register.html')



@app.route('/show_list')
def show_list():
    if 'username' in session:
        return render_template("lists.html", 
                                lists = mongo.db.lists.find(),
                                users = mongo.db.users.find_one({'name': session['username']}))
    return render_template("lists.html", 
                            lists = mongo.db.lists.find())


@app.route('/view_lists/<list_id>')
def view_lists(list_id):
    lists = mongo.db.lists
    list_db=lists.find_one({'_id': ObjectId(list_id)})
    if 'username' in session:
        return render_template("show_list.html", 
                                lists=list_db, 
                                listName = mongo.db.lists.find(),
                                users = mongo.db.users.find_one({'name': session['username']}))
    return render_template("show_list.html", 
                            lists=list_db, 
                            listName = mongo.db.lists.find())



@app.route('/create_list')
def create_list():
    return render_template("create_list.html", 
                            lists=mongo.db.lists.find(),
                            users = mongo.db.users.find_one({'name': session['username']}))








@app.route('/insert_list', methods=['POST'])
def insert_list():
    lists = mongo.db.lists
    if request.method == "POST":
        form = request.form.to_dict()
        myListObject = [
            {
            "list_object_number": form['list_object_number_1'],
            "list_object_name": form['list_object_name_1'],
            "list_object_description": form['list_object_description_1']         
            },
             {
            "list_object_number": form['list_object_number_2'],
            "list_object_name": form['list_object_name_2'],
            "list_object_description": form['list_object_description_2']         
            },
            {
            "list_object_number": form['list_object_number_3'],
            "list_object_name": form['list_object_name_3'],
            "list_object_description": form['list_object_description_3']         
            },
             {
            "list_object_number": form['list_object_number_4'],
            "list_object_name": form['list_object_name_4'],
            "list_object_description": form['list_object_description_4']         
            },
            {
            "list_object_number": form['list_object_number_5'],
            "list_object_name": form['list_object_name_5'],
            "list_object_description": form['list_object_description_5']         
            },
             {
            "list_object_number": form['list_object_number_6'],
            "list_object_name": form['list_object_name_6'],
            "list_object_description": form['list_object_description_6']         
            },
            {
            "list_object_number": form['list_object_number_7'],
            "list_object_name": form['list_object_name_7'],
            "list_object_description": form['list_object_description_7']         
            },
             {
            "list_object_number": form['list_object_number_8'],
            "list_object_name": form['list_object_name_8'],
            "list_object_description": form['list_object_description_8']         
            },
            {
            "list_object_number": form['list_object_number_9'],
            "list_object_name": form['list_object_name_9'],
            "list_object_description": form['list_object_description_9']         
            },
             {
            "list_object_number": form['list_object_number_10'],
            "list_object_name": form['list_object_name_10'],
            "list_object_description": form['list_object_description_10']         
            }
        ]
        
        obj = {
            "list_name": form['list_name'],
            'image_file': form['image_file'],
            "list_objects": myListObject,
            "user": session['username']
        }
        lists.insert_one(obj)
    
    return redirect(url_for('show_list'))                     


@app.route('/edit_list/<list_id>')
def edit_list(list_id):
    the_list=mongo.db.lists.find_one({"_id":ObjectId(list_id)})
    return render_template('edit_list.html',
                            lists=the_list,
                            users = mongo.db.users.find_one({'name': session['username']}))


@app.route('/update_list/<list_id>', methods=["POST"])
def update_list(list_id):      
    myListObject = [
                {
                "list_object_number": request.form.get('list_object_number_1'),
                "list_object_name": request.form.get('list_object_name_1'),
                "list_object_description": request.form.get('list_object_description_1')         
                },
                {
                "list_object_number": request.form.get('list_object_number_2'),
                "list_object_name": request.form.get('list_object_name_2'),
                "list_object_description": request.form.get('list_object_description_2')         
                },
                {
                "list_object_number": request.form.get('list_object_number_3'),
                "list_object_name": request.form.get('list_object_name_3'),
                "list_object_description": request.form.get('list_object_description_3')         
                },
                {
                "list_object_number": request.form.get('list_object_number_4'),
                "list_object_name": request.form.get('list_object_name_4'),
                "list_object_description": request.form.get('list_object_description_4')         
                },
                {
                "list_object_number": request.form.get('list_object_number_5'),
                "list_object_name": request.form.get('list_object_name_5'),
                "list_object_description": request.form.get('list_object_description_5')         
                },
                {
                "list_object_number": request.form.get('list_object_number_6'),
                "list_object_name": request.form.get('list_object_name_6'),
                "list_object_description": request.form.get('list_object_description_6')         
                },
                {
                "list_object_number": request.form.get('list_object_number_7'),
                "list_object_name": request.form.get('list_object_name_7'),
                "list_object_description": request.form.get('list_object_description_7')         
                },
                {
                "list_object_number": request.form.get('list_object_number_8'),
                "list_object_name": request.form.get('list_object_name_8'),
                "list_object_description": request.form.get('list_object_description_8')         
                },
                {
                "list_object_number": request.form.get('list_object_number_9'),
                "list_object_name": request.form.get('list_object_name_9'),
                "list_object_description": request.form.get('list_object_description_9')         
                },
                {
                "list_object_number": request.form.get('list_object_number_10'),
                "list_object_name": request.form.get('list_object_name_10'),
                "list_object_description": request.form.get('list_object_description_10')         
                }
            ]  
    lists = mongo.db.lists.update( {'_id': ObjectId(list_id)},
        {
            'list_name':request.form.get('list_name'),
            'image_file': request.form.get('image_file'),
            "user": session['username'],
            "list_objects": myListObject
        })
    return redirect(url_for('show_list'))


@app.route('/delete_list/<list_id>')
def delete_list(list_id):
    mongo.db.lists.remove({'_id': ObjectId(list_id)})
    return redirect(url_for('show_list'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=False)
