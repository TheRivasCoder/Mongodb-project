from flask import Flask, jsonify, request
# Encrypt password
from passlib.hash import pbkdf2_sha256
# Import database (db) from app.py file
from app import db
# Package to create object id for user
import uuid

class User:
    
    def signup(self):
        
        # Create the user object
        user = {
            "_id": uuid.uuid4().hex, # Create user id
            "name": request.form.get('name'), # Gets name from "signup_form" form in home.html
            "email": request.form.get('email'), # Gets email from "signup_form" form in home.html
            "password": request.form.get('password') # Gets password from "signup_form" form in home.html
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # If user email is already in database then return error
        if db.first_collection.find_one({ "email": user['email']}):
            return jsonify({ "error": "Email address already in use"}), 400

        # Database collection 'users' will have app user inserted
        db.first_collection.insert_one(user)

        return jsonify(user), 200
