from flask import Flask, request
from app import app
from user.models import User
from app import app
from app import db
import pymongo
#from pymongo import MongoClient

#cluster = MongoClient("mongodb+srv://dbUser:projectx@cluster0.zekyr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = cluster["client"]
#collection= db["client"]

@app.route('/')
def homepage():
  return User().homepage()

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/fuelform')
def fuelform():
  return User().fuelform()

@app.route('/user/fuelform', methods=['POST'])
def fillfuelform():
  return User().fillfuelform()


@app.route('/user/fuelhistory')
def fuelhistory():
  return User().fuelhistory()

@app.route('/user/profile')
def rendProfile():
  return User().rendProfile()

@app.route('/user/profile', methods=['POST'])
def profile():
  return User().profile()

@app.route('/user/login')
def signlog():
  return User().signlog()


@app.route('/user/login', methods=['POST'])
def login():
  return User().login()
