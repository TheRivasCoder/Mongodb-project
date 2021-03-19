# Packages in virtual env: mongopy3
from flask import Flask, render_template
import pymongo


app = Flask(__name__)

# Database
cluster = pymongo.MongoClient("mongodb+srv://ChrisRivas:mongodbpassword@testcluster.aurrw.mongodb.net/database_name?retryWrites=true&w=majority", 27017)
db = cluster["database_name"]
collection = db["first_collection"]


# From file user import file routes.py
# This import must be inside app
from user import routes


@app.route('/')
def home():
    # Renders home page 
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    # Renders dashboard page
    return render_template('dashboard.html')


    
