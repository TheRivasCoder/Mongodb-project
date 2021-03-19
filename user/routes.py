from flask import Flask
#from file app.py import app
from app import app
#from user folder inside models.py file import User class
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

