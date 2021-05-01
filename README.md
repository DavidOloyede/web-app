#Might have to enter http://127.0.0.1:5000/user/dashboard/ after clicking log in 
#In Terminal for web-app folder (windows)

> py -m virtualenv env

> env\Scripts\activate

> pip install dnspython flask pymongo passlib

> set FLASK_APP=app.py

> flask run

#UnitTest
> pip install pytest coverage pytest-co

> pytest --cov=unittest --cov-report=html

