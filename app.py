import os
from flask import Flask, render_template, redirect, request, url_for, session
import bcrypt
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.secret_key = os.getenv("SECRET", "mySecretKey")
app.config["MONGO_DBNAME"] = "topTenDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


"""def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')"""

@app.route('/')


# Route to homepage
@app.route('/home')
def home_page():
    if 'username' in session:
        return render_template("logged-in-home.html", users = mongo.db.users.find_one({'name': session['username']}))
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
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


@app.route('/account')
def account():
    return render_template('account.html', users = mongo.db.users.find_one({'name': session['username']}))






@app.route('/lists')
def show_lists():
    return render_template("lists.html",
                            lists=list(mongo.db.lists.find()))


@app.route('/show_list/<lists_id>')
def show_list(lists_id):
    return render_template("show_list.html", 
                            lists=mongo.db.lists.find_one({"_id": ObjectId(lists_id)}))


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
