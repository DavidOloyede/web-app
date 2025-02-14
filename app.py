from flask import Flask, render_template, session, redirect
import unittest
import urllib
from functools import wraps
import pymongo
from pymongo import MongoClient
# from flask_pymongo import PyMongo
#from pprint import pprint
from passlib.hash import pbkdf2_sha256
import uuid

app = Flask(__name__)
app.debug = True
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
cluster = MongoClient("mongodb+srv://dbUser:projectx@cluster0.zekyr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["client"]
collection= db["client"]
#collection.insert_one( {"foo" : "bar" }) #add a document to testdb.testcol


# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):  
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')


if __name__ == "__main__":
  app.run(debug=True)
