# Import Flask
from flask import Flask
# From file app.py import app
from app import app
# From user folder inside models.py file import User class
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

