from flask import Flask, jsonify, request, session, redirect, render_template
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200
  
  def signout(self):
    session.clear()
    session.pop('user', None)
    return redirect('/')

  def fuelform(self):
    if "user" in session:
      user = session["user"]
    return render_template('fuelQform.html')
  
  def fillfuelform(self):
    print(request.form)
    # if(request.form.get('gallonsRequested')!=''):
    #   totalAmountPrice = request.form.get('totalAmountPrice')+ " "+ request.form.get('dateRequested')+" " + request.form.get('gallonsRequested')
    # elif(request.form.get('gallonsRequested')==''):
    #   totalAmountPrice = request.form.get('totalAmountPrice')+ " "+ request.form.get('dateRequested')+" " + request.form.get('gallonsRequested')
    # user= db.users.find_one({
    #   "_id": session['user']['_id']
    # })
    return self.fuelform()
  
  def fuelhistory(self):
    if "user" in session:
      user = session["user"]
    return render_template('fuelQHistory.html')

  def rendProfile(self):
    if "user" in session:
      user= session["user"]
    return render_template('profile.html')
  
  def profile(self):
    print(request.form)
    if(request.form.get('add2')!=''):
      address= request.form.get('add1')+" "+request.form.get('add2')+", "+request.form.get('city')+", "+request.form.get('state')+" "+request.form.get('zip')
    elif(request.form.get('add2')==''):
      address= request.form.get('add1')+", "+request.form.get('city')+", "+request.form.get('state')+" "+request.form.get('zip') 
    user= db.users.find_one({
      "_id": session['user']['_id']
    })


    if user:
      db.users.update({"_id": session['user']['_id']}, {"$set": {"address": address, "state": request.form.get('state')}})
      session['user']['address']= address
      return redirect('/user/dashboard/')
    else:
      return jsonify({ "error": "Invalid login credentials" }), 401

      # if user:
      #   db.users.update({"_id": session['user']['_id']}, {"$set": {"gallonsRequested": gallonsRequested, "dateRequested": request.form.get('dateRequested')}})
      #   session['user']['gallonsRequested']= gallonsRequested
      #   return redirect('/user/dashboard/')
      # else:
      #   return jsonify({ "error": "Invalid login credentials" }), 401
    #if(db.users.update_one({"_id": session['user']['_id']}, {"$set": {"address": address}})):
    #  return self.profile(user)#jsonify({ "message": "Succesful Set Profile Info" }), 200
  
  def signlog(self):
    return render_template('login.html')

  def homepage(self):
    return render_template('index.html')
  
  def login(self):
    session.clear()
    session.pop('user', None)

    if request.form.get('login'):
      user = db.users.find_one({
        "email": request.form.get('email')
      })
      #if(user):
        #print(request.form)

      if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
        return self.start_session(user)
      else:
        return jsonify({ "error": "Invalid login credentials" }), 401
    elif request.form.get('signup'):
      user = {
        "_id": uuid.uuid4().hex,
        "name": request.form.get('name'),
        "email": request.form.get('emailAdd'),
        "password": request.form.get('password'),
      }

      # Encrypt the password
      user['password'] = pbkdf2_sha256.encrypt(user['password'])
      # Check for existing email address
      if db.users.find_one({ "email": user['email'] }):
        return jsonify({ "error": "Email address already in use" }), 400

      if db.users.insert_one(user):
        return self.start_session(user)

      return jsonify({ "error": "Signup failed" }), 400
