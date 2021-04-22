from flask import Flask, render_template, session, redirect
from functools import wraps
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
cluster = MongoClient("mongodb+srv://dbUser:projectx@cluster0.zekyr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["client"]
collection= db["client"]


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

@app.route('/login/')
def home():
  return render_template('login.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

if __name__ == "__main__":
  app.run(debug=True)
