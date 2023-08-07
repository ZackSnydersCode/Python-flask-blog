from flask import Flask, render_template, request,jsonify,redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import make_response
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
import os
import random
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/myGirls'
mongo = PyMongo(app)

fileHolder = os.path.join('static', 'files')
app.config["ALBUM_FILES"] = fileHolder

@app.route('/profile')
def save_data():
    return render_template('profile.html')

@app.route('/data',methods=['POST','GET'])
def album():
   mongo.db.Data.insert_one({"msg":"from Git"})
   return render_template('package.html')

if __name__ == '__main__':
    app.run(debug=True)
