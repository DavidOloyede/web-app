from flask import Flask
from app import app
from user.models import User

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

@app.route('/user/fuelhistory')
def fuelhistory():
  return User().fuelhistory()

@app.route('/user/login')
def signlog():
  return User().signlog()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()