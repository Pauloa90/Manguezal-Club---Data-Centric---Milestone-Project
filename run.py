import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Linking my app to MongoDB
app.config["MONGO_DBNAME"] = 'reviewmanguezal'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-73r36.mongodb.net/reviewmanguezal?retryWrites=true&w=majority'

# Creating a Instance for Pymongo
mongo = PyMongo(app)

@app.route("/manguezalclub")
def manguezalclub():
    return render_template('manguezalclub.html', manguezalclub=mongo.db.review.find())

@app.route("/")
@app.route("/manguezalclub")
def get_reviews():
    return render_template("manguezalclub.html",
        manguezalclub=mongo.db.review.find())

@app.route("/addreview")
def addreview():
    return render_template("addreview.html", 
        categories=mongo.db.categories.find())

@app.route("/insert_review", methods=['POST'])
def insert_review():
    review = mongo.db.review
    review.insert_one(request.form.to_dict())
    return redirect(url_for('manguezalclub'))




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)