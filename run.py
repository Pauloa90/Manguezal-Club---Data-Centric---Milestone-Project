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
def index():
    return render_template("index.html")


@app.route("/addreview")
def addreview():
    return render_template("addreview.html", 
        categories=mongo.db.categories.find())

@app.route("/insert_review", methods=['POST'])
def insert_review():
    review = mongo.db.review
    review.insert_one(request.form.to_dict())
    return redirect(url_for('manguezalclub'))

@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.review.find_one({"_id": ObjectId(review_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_review.html', review=the_review, categories = all_categories)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)